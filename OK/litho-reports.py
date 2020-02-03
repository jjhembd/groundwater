import sys
import pandas
import geojson

def printReport(row, lithologies, outdir):
    lon = float(row['LONGITUDE'])
    lat = float(row['LATITUDE'])
    point = geojson.Point((lon, lat))

    ID = row['WELL_ID']
    lithology = ""
    if (ID in lithologies):
        lithology = '[' + lithologies[ID] + ']'
    props = {
            'Longitude': str(row['LONGITUDE']),
            'Latitude': str(row['LATITUDE']),
            'State': 'OK',
            'County': str(row['COUNTY']),
            'ID': str(ID),
            'Elevation': str(row['ELEVATION']),
            'Depth': str(row['TOTAL_DEPTH']),
            'Date': str(row['CONST_DATE']),
            'Company': str(row['FIRM_NAME']),
            'Operator': str(row['OPERATOR_ID']),
            'Owner': str(row['OWNER_NAME_x']),
            'Usage': str(row['USE_CLASS']),
            'Lithology': lithology
            }

    feature = geojson.Feature(geometry=point, properties=props)
        
    fname = outdir + '/' + str(ID) + '.json'
    f = open(fname, "w")
    f.write(geojson.dumps(feature, indent=2))
    f.close()

    print 'Finished well ID ' + str(ID)
    return

def processFiles(main_file, logs_file, lith_file, outdir):
    # Read the main and logs files, and merge them
    main = pandas.read_csv(main_file)
    logs = pandas.read_csv(logs_file)
    data = main.merge(logs, left_on='SITE_ID', right_on='WELL_ID')

    # Concatenate the columns of the lithology descriptions into a string
    # representation of a JSON array
    lith = pandas.read_csv(lith_file)
    lithStrings = pandas.DataFrame({
        'ID': lith['SITE_ID'],
        'LayerString': '[' + lith['LITHO_TOP'].astype(str) + ',' \
                + lith['LITHO_BOT'].astype(str) + ',' \
                + lith['LITHO_MTR'].astype(str) + ']'
        })
    del lith
    # Group by well number, concatenate again, and convert to a dictionary
    lithDict = lithStrings \
            .groupby('ID') \
            .agg(lambda x: x.str.cat(sep=',')) \
            .to_dict()['LayerString']
    del lithStrings

    for index, row in data.iterrows():
        printReport(row, lithDict, outdir)

    return

if len(sys.argv) < 5:
    print('Usage:\n  python ' + sys.argv[0] + ' main_file logs_file lithology_file output_directory')
else:
    processFiles(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
