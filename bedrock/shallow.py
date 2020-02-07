import pandas

maxdepth = 15

# Read the pre-processed lithology descriptions with rippability classification
lith = pandas.read_csv('data/rippability.csv')

# Discard layers where LITHO_TOP is missing or > maxdepth
def is_shallow(depth):
    if pandas.isna(depth): return False
    return depth <= maxdepth

shallow = lith.loc[lith['LITHO_TOP'].map(is_shallow)] \
        .loc[lith['RIPPABILITY'].map(lambda x: not pandas.isna(x))]

# Group by SITE_ID, and find the lowest rippability values
rippabilities = shallow.groupby('SITE_ID')['RIPPABILITY'].agg(min)

# TODO: Discard wells that don't penetrate to max_depth

# Write out to a new CSV
rippabilities.to_csv('data/shallow_rippability.csv')
