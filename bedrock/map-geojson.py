import sys
import pandas
import geojson
from datetime import datetime

nanval = float('NaN')

def get_date(datestring):
    if pandas.isna(datestring): return str(nanval)
    year = int(datestring.split('/')[0])
    if year > datetime.now().year: return str(nanval)
    return pandas.to_datetime(datestring).strftime('%Y-%m-%d')

def printFeature(row, file):
    lon = float(row['LONGITUDE'])
    lat = float(row['LATITUDE'])
    point = geojson.Point((lon, lat))

    props = {
            'State': 'OK',
            'ID': str(row['WELL_ID']),
            'Depth': str(row['TOTAL_DEPTH']),
            'Rippability': str(row['RIPPABILITY']),
            'Date': get_date(row['CONST_DATE']),
            'Company': str(row['FIRM_NAME']),
            }

    feature = geojson.Feature(geometry=point, properties=props)
    file.write(geojson.dumps(feature) + ',\n')

    return

def processFiles():
    # Read the main, logs, and rippability files, and merge them
    main = pandas.read_csv('data/WL_Main.csv')
    logs = pandas.read_csv('data/Reported_Well_Logs.csv')
    data = main.merge(logs, left_on='SITE_ID', right_on='WELL_ID')

    rips = pandas.read_csv('data/shallow_rippability.csv')
    merge = data.merge(rips, left_on='SITE_ID', right_on='SITE_ID')

    print('Finished data merging. Writing to output file...')

    # Initialize the GeoJSON
    f =  open('data/rippability_map.geojson', "w")
    f.write('{"type": "FeatureCollection", "features": [\n')

    # Write out the desired fields, renaming as needed
    for index, row in merge.iterrows():
        printFeature(row, f)

    # Close file
    f.write(']}')
    f.close()

    return

processFiles()
