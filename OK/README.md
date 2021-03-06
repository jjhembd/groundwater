Source: ESRI File Geodatabase, updated monthly  
www.owrb.ok.gov/maps/data/layers/Groundwater/Well\_Logs.zip

The raw GeoDatabase is converted to CSV as follows:
```bash
ogr2ogr -overwrite -progress -f csv output_directory input_directory/input_database.gdb
```
The directory `output_directory` will be created by this command

We then generate two files: a single GeoJSON from which map tiles are made
(after combining with other states), and one GeoJSON per well, for reporting
more information when a user clicks on a well on the map.

The per-well GeoJSONs are uploaded to an S3 bucket, prefixed by a state code.
The AWS CLI doesn't seem to allow copying 200,000 files at once.
(this could be a bash limitation on number of arguments?)
Hence we must split into subfolders, and copy one at a time, i.e.,

```bash
aws s3 cp xxxxx/  s3://internal.earthpeel.com/groundwater/OK/ --recursive
```

Note that with 100k files, the above command may hang for 5-10 minutes,
before starting to do anything.

To speed up the process, copy several folders simultaneously, from different
terminal windows
