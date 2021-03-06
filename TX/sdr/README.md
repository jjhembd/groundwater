Raw download is already a pipe-delimited file.
Data must first be fixed following the directions in fixing-input.txt

We then generate two files: a single GeoJSON from which map tiles are made
(after combining with other states), and one GeoJSON per well, for reporting
more information when a user clicks on a well on the map.

For example:
```bash
# cd data/<download-date>/
# python litho-reports.py \
    fix-encoding/WellData_select-fields.txt \
    fix-encoding/WellLithology_fix-delimiters.txt \
    fix-encoding/WellBoreHole.txt \
    json
# python map-geojson.py \
    fix-encoding/WellData_select-fields.txt \
    fix-encoding/WellBoreHole.txt \
    > TX-SDR-map.geojson
```

The per-well GeoJSONs are uploaded to an S3 bucket, prefixed by a state code.
The AWS CLI doesn't seem to allow copying 200,000 files at once.
(this could be a bash limitation on number of arguments?)
Hence we must split into subfolders, and copy one at a time, i.e.,

```bash
aws s3 cp xxxxx/  s3://internal.earthpeel.com/groundwater/OK/ --recursive
```

Note that with 100k files, the above command may hang for 5-10 minutes,
before starting to do anything.
