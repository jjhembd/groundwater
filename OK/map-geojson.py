import sys
import pandas
import geojson

def printFeature(row):
    lon = float(row['LONGITUDE'])
    lat = float(row['LATITUDE'])
    point = geojson.Point((lon, lat))

    props = {
            'State': 'OK',
            'ID': str(row['WELL_ID']),
            'Depth': str(row['TOTAL_DEPTH']),
            'Date': str(row['CONST_DATE']),
            'Company': str(row['FIRM_NAME']),
            }

    print geojson.dumps(geojson.Feature(geometry=point, properties=props)) + ','

    return

def processFiles(main_file, logs_file):
    # Read the main and logs files, and merge them
    main = pandas.read_csv(main_file)
    logs = pandas.read_csv(logs_file)
    data = main.merge(logs, left_on='SITE_ID', right_on='WELL_ID')

    # Initialize the GeoJSON
    print('{"type": "FeatureCollection", "features": [')

    # Write out the desired fields, renaming as needed
    for index, row in data.iterrows():
        printFeature(row)

    # Close file
    print(']}')
    return

if len(sys.argv) < 3:
    print('Usage:\n  python ' + sys.argv[0] + ' main_file logs_file > output.geojson')
else:
    processFiles(sys.argv[1], sys.argv[2])
