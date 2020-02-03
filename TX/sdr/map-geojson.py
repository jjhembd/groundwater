import sys
import pandas
import geojson

def printFeature(row, depths):
    lon = float(row['CoordDDLong'])
    lat = float(row['CoordDDLat'])
    point = geojson.Point((lon, lat))

    ID = row['WellReportTrackingNumber']
    depth = ""
    if (ID in depths):
        depth = depths[ID]

    props = {
            'Longitude': str(row['CoordDDLong']),
            'Latitude': str(row['CoordDDLat']),
            'State': 'TX',
            'ID': str(ID),
            'Depth': str(depth),
            'Date': str(row['DrillingEndDate']),
            'Company': str(row['CompanyName']),
            }

    print geojson.dumps(geojson.Feature(geometry=point, properties=props)) + ','

    return

def processFiles(data_file, bore_file):
    # Read the data and borehole files
    data = pandas.read_csv(data_file, delimiter='|', quoting=3)
    bore = pandas.read_csv(bore_file, delimiter='|', quoting=3)

    # Get the total depths of each well from the borehole info
    depths = bore \
            .groupby('WellReportTrackingNumber')['BottomDepth'] \
            .max() \
            .to_dict()
    del bore

    # Initialize the GeoJSON
    print('{"type": "FeatureCollection", "features": [')

    # Write out the desired fields, renaming as needed
    for index, row in data.iterrows():
        printFeature(row, depths)

    # Close file
    print(']}')
    return

if len(sys.argv) < 3:
    print('Usage:\n  python ' + sys.argv[0] + ' data_file boreholes_file > output.geojson')
else:
    processFiles(sys.argv[1], sys.argv[2])
