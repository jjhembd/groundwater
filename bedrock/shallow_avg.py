import pandas

maxz = 20

# Read the pre-processed lithology descriptions with rippability classification
lith = pandas.read_csv('data/rippability.csv')

# Discard layers where LITHO_TOP is missing or > maxdepth
def is_shallow(depth):
    if pandas.isna(depth): return False
    return depth < maxz

shallow = lith.loc[lith['LITHO_TOP'].map(is_shallow)] \
        .loc[lith['LITHO_BOT'] > lith['LITHO_TOP']] \
        .loc[lith['RIPPABILITY'].map(lambda x: not pandas.isna(x))]

# Scale rippabilities by the fraction of maxz covered by that layer
shallow['thickness'] = shallow['LITHO_BOT'].clip(0, maxz) - shallow['LITHO_TOP']
shallow['norm_rip'] = shallow['RIPPABILITY'] * shallow['thickness'] / maxz

sums = shallow.groupby('SITE_ID')[['thickness', 'norm_rip']].agg(sum)
complete = sums.loc[sums['thickness'] == maxz].reset_index()
complete.columns = ['SITE_ID', 'thickness', 'RIPPABILITY']

# Read the logs file, and merge to get longitude / latitude
logs = pandas.read_csv('data/Reported_Well_Logs.csv')
merge = logs.merge(complete, left_on='WELL_ID', right_on='SITE_ID')

# Write out to a new CSV file
outfile = 'data/lonlatrip_0-20_t2.csv'
columns = ['SITE_ID', 'LONGITUDE', 'LATITUDE', 'RIPPABILITY']
merge[columns].to_csv(outfile, encoding='utf-8', index=False)
