import pandas

# Define a box around the area of interest
minLon = -97.0
minLat = 33.75
maxLon = -96.3
maxLat = 36.0

# Read the main and logs files, and merge them
main = pandas.read_csv('data/WL_Main.csv')
logs = pandas.read_csv('data/Reported_Well_Logs.csv')
data = main.merge(logs, left_on='SITE_ID', right_on='WELL_ID')
del main, logs

# Limit to the area of interest
lonflag = data['LONGITUDE'].between(minLon, maxLon)
latflag = data['LATITUDE'].between(minLat, maxLat)
boxdata = data[lonflag & latflag]

# Keep only the needed columns, and standardize their names
trimlogs = pandas.DataFrame({
    'ID': boxdata['WELL_ID'],
    'Longitude': boxdata['LONGITUDE'],
    'Latitude': boxdata['LATITUDE'],
    'Elevation': boxdata['ELEVATION'],
    'State': 'OK',
    'County': boxdata['COUNTY'],
    'Date': pandas.to_datetime(boxdata['CONST_DATE']),
    'Company': boxdata['FIRM_NAME'],
    'Operator': boxdata['OPERATOR_ID'],
    'Owner': boxdata['OWNER_NAME_x'],
    'Usage': boxdata['USE_CLASS']
    })

# Write out to a new csv
column_order = ['ID', 
        'Longitude', 'Latitude', 'Elevation',
        'State', 'County', 
        'Date', 'Company', 'Operator', 
        'Owner', 'Usage']

trimlogs[column_order].to_csv('data/AOI_t1.csv', encoding='utf-8', index=False, date_format="%Y-%m-%d")
