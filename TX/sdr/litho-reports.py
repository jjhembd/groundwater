import sys
import pandas
import geojson

def printReport(row, lithologies, depths, outdir):
    lon = float(row['CoordDDLong'])
    lat = float(row['CoordDDLat'])
    point = geojson.Point((lon, lat))

    ID = row['WellReportTrackingNumber']
    lithology = ""
    if (ID in lithologies):
        lithology = '[' + lithologies[ID] + ']'
    depth = ""
    if (ID in depths):
        depth = depths[ID]
    props = {
            'Longitude': str(row['CoordDDLong']),
            'Latitude': str(row['CoordDDLat']),
            'State': 'TX',
            'County': str(row['County']),
            'ID': str(ID),
            'Elevation': str(row['Elevation']),
            'Depth': str(depth),
            'Date': str(row['DrillingEndDate']),
            'Company': str(row['CompanyName']),
            'Operator': str(row['DrillerName']),
            'Owner': str(row['OwnerName']),
            'Usage': str(row['ProposedUse']),
            'Lithology': lithology
            }

    feature = geojson.Feature(geometry=point, properties=props)

    fname = outdir + '/' + str(ID) + '.json'
    f = open(fname, "w")
    f.write(geojson.dumps(feature, indent=2))
    f.close()

    print 'Finished well ID ' + str(ID)
    return

def processFiles(data_file, lith_file, bore_file, outdir):
    data = pandas.read_csv(data_file, delimiter='|', quoting=3)
    lith = pandas.read_csv(lith_file, delimiter='|', quoting=3)
    bore = pandas.read_csv(bore_file, delimiter='|', quoting=3)

    # Concatenate the columns of the lithology descriptions into a string
    lithStrings = pandas.DataFrame({
        'ID': lith['WellReportTrackingNumber'],
        'LayerString': '[' + lith['TopDepth'].astype(str) + ',' \
                + lith['BottomDepth'].astype(str) + ',' \
                + lith['LithologyDescription'].astype(str) + ']'
        })
    del lith
    # Group by well number, concatenate again, and convert to a dictionary
    lithDict = lithStrings \
            .groupby('ID') \
            .agg(lambda x: x.str.cat(sep=',')) \
            .to_dict()['LayerString']
    del lithStrings

    # Get the total depths of each well from the borehole info
    depths = bore \
            .groupby('WellReportTrackingNumber')['BottomDepth'] \
            .max() \
            .to_dict()
    del bore

    for index, row in data.iterrows():
        printReport(row, lithDict, depths, outdir)

    return

if len(sys.argv) < 5:
    print('Usage:\n  python ' + sys.argv[0] + ' data_file lithology_file borehole_file output_directory')
else:
    processFiles(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
