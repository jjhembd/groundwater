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

# Discard wells that do not sample the entire interval [0, maxz]
complete = shallow.groupby('SITE_ID') \
        .filter(lambda x: x['thickness'].sum() == maxz)

# Sum the normalized rippability at each well
avg_rip = complete.groupby('SITE_ID')['norm_rip'].agg(sum)

# Write out to a new CSV
avg_rip.to_csv('data/avg_rippability_0-20.csv', header=['RIPPABILITY'])
