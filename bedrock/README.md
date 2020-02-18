We have 900k lithology descriptions in OK, 3.8m in TX. That's likely less than
half of the total&mdash;many are still in scanned, handwritten documents.
Note the effort: a busy driller in his coveralls, takes time to clean his
hands, and pick up pencil and paper to note:

"100 - 135 ft.: Red clay with streaks of fine white sand"

And repeat for thousands of drillers, millions of wells...
Note the value: 4.6 million descriptions of the layers under our feet!

How can we review them? We assume the layers extend for some distance--
many entries should be describing the same thing at different locations.
So we load the OK data into a Pandas dataframe, and count the number of 
unique values in the `LITHO_MTR` field:

```
>>> lith['LITHO_MTR'].value_counts()
shale                                                      49319
clay                                                       32337
sandrock                                                   28838
sand                                                       22091
Clay                                                       18247
red clay                                                   18061
red shale                                                  17054
sandstone                                                  15461
...
Name: LITHO_MTR, Length: 118120, dtype: int64
```

That's out of 893,399 rows. So each layer is repeated <9x?
Well, obviously the formatting is not consistent. Note the various
capitalizations... Let's fix that:

```
>>> lith['LITHO_MTR'].str.lower().value_counts()
shale                                                        77336
clay                                                         62100
sandrock                                                     41308
sand                                                         35883
red clay                                                     27628
red shale                                                    27216
sand rock                                                    25877
sandstone                                                    21579
...
Name: LITHO_MTR, Length: 104442, dtype: int64
```

The peak got taller, but the tail isn't much shorter.
Some obvious fixes: fix misspellings, expand abbreviations, standardize
compound words ('sandrock' and 'sand rock' are the same thing).
But these are nontrivial tasks. First we need to separate words. The delimiter
could be a space, multiple spaces, commas, slashes, dashes... And what to do 
with 'w/'?
Then, ideally, we want to put them back together as they were.

Looking deeper, we can see that there are really 5 things being described:
- Material
- Grain size
- Color
- Strength (how solid/crumbly)
- Wetness

Now there is some overlap: for example, the words 'clay', 'silt', 'sand'
are describing different grain sizes, but we assume clay and sand are probably
also different minerals. So by 'Grain size', we mean only words like 'fine',
'medium', 'coarse'--or even the numerical grain sizes given by some drillers.
Also, 'shale' is just lithified 'clay', but we consider them as different
materials rather than the same material with different strengths.

...

```bash
tippecanoe -o data/2020-02-07_OKRIP.mbtiles \
  -b 20 -z 9 -g 2 -m150000 \
  --drop-densest-as-needed --extend-zooms-if-still-dropping \
  data/rippability_map.geojson
Layer name: rippability_map
Mapbox tileset ID: jhembd.8rpw4r9q
```

## Generating an interpolated map
We first convert to Web Mercator, so the interpolation filters will be
isotropic (wrong word?). Using ogr2ogr:
```bash
ogr2ogr data/avg_rip_webmerc.geojson -t_srs "EPSG:3857" data/avg_rippability.geojson
```

Next, for interpolation, we will need to know the extent in Web Mercator. 
First confirm the layer name:
```bash
# ogrinfo data/avg_rip_webmerc.geojson
INFO: Open of `data/avg_rip_webmerc.geojson'
      using driver `GeoJSON' successful.
1: avg_rippability (Point)
```

Now get a summary of the layer:
```bash
# ogrinfo data/avg_rip_webmerc.geojson avg_rippability -so
INFO: Open of `data/avg_rip_webmerc.geojson'
      using driver `GeoJSON' successful.

Layer name: avg_rippability
Geometry: Point
Feature Count: 138049
Extent: (-11466139.430207, 3982996.182705) - (-10512476.929808, 4439413.443316)
...
```

As a first try of interpolation, we test `gdal_grid`:
```bash
gdal_grid -a invdist:power=2.0:smoothing=1.0:radius1=1000:radius2=1000 \
  -txe -11467000 -10512000 -tye 3982000 4440000 -outsize 955 458 \
  -of GTiff -l avg_rippability -zfield "Rippability" \
  data/avg_rip_webmerc.geojson data/avg_rip_1000x1000.tiff
```

BUT this doesn't look good... need some way of QC'ing raw values of the
interpolation--maybe not TIFF output?
Reference: https://gdal.org/programs/gdal_grid.html#interpolation-algorithms

This works on a 5-point test file:
gdal_grid -l rippability -zfield Rippability test_rip.geojson test_grid.tiff

QC as follows: first check an XYZ file:
gdal_translate -of XYZ test_grid.tiff test_grid.xyz

Then an auto-scaled PNG:
gdal_translate -of PNG -scale test_grid.tiff test_grid.png

BUT this result is all zero in the z-column:
gdal_translate -of XYZ -scale avg_rip_1000x1000.tiff avg_rip_1000x100_t2.xyz

A flow that works, though awkward:
0. Convert to the Oklahoma North state plane projection
ogr2ogr avg_rip_stateplane.geojson -t_srs "EPSG:6552" avg_rippability.geojson 
1. Linear interpolation
gdal_grid -a linear:radius=1000 -l rippability -zfield Rippability -outsize 2048 1024 avg_rip_stateplane.geojson avg_rip_stateplane_t6.tiff
2. Flip the y-axis
gdalwarp avg_rip_stateplane_t6.tiff avg_rip_stateplane_t6flip.tiff
3. Convert to PNG
gdal_translate -of PNG -scale avg_rip_stateplane_t6flip.tiff avg_rip_stateplane_t6.png
