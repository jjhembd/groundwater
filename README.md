# Groundwater well data collection

This repository collects scripts for processing data from groundwater wells,
from a variety of government sources (mostly separate sources per 
state/province).

The data itself is not stored here. The scripts assume the data is in
subdirectories with paths as follows:
```bash
/<StateCode>/data/<dateDownloaded>/
```

## Format for output data
The scripts for each state output two datasets:
- A GeoJSON FeatureCollection containing longitude, latitude, State, and ID for
  each well. These are used to generate vector tiles for map displays (after
  combining all states). Template: `template-map.json`
- A GeoJSON Feature containing detailed lithology information for each well.
  These files can be stored in an S3 bucket and retrieved one at a time.
  Template: `template-report.json`

## Input data sources
See the README in each state directory
