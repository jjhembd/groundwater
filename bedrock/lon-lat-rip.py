import pandas

def processFiles():
    # Read the main and rippability files, and merge them
    logs = pandas.read_csv('data/Reported_Well_Logs.csv')
    rips = pandas.read_csv('data/avg_rippability_0-20.csv')
    merge = logs.merge(rips, left_on='WELL_ID', right_on='SITE_ID')

    outfile = 'data/lonlatrip_0-20.csv'
    columns = ['SITE_ID', 'LONGITUDE', 'LATITUDE', 'RIPPABILITY']
    merge[columns].to_csv(outfile, encoding='utf-8', index=False)

    return

processFiles()
