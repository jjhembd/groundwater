import pandas
import description
import categorize

# Get raw file, report statistics
lith = pandas.read_csv('data/WL_Lithology.csv')
numvals = lith['LITHO_MTR'].value_counts().shape[0]
print('Number of descriptions in raw file: ' + str(numvals))

# Fix spelling and other problems
lith['LITHO_MTR'] = lith['LITHO_MTR'].map(description.fix, na_action='ignore')
numvals = lith['LITHO_MTR'].value_counts().shape[0]
print('After fixing common mis-spellings: ' + str(numvals))

# Add rippability classifications
lith['RIPPABILITY'] = lith['LITHO_MTR'].map(categorize.rippability, na_action='ignore')

# Fix formatting of top and bot columns
lith['LITHO_TOP'] = lith['LITHO_TOP'].map('{:.0f}'.format)
lith['LITHO_BOT'] = lith['LITHO_BOT'].map('{:.0f}'.format)

# Write out to a new file
column_order = ['SITE_ID', 'LITHO_TOP', 'LITHO_BOT', 'LITHO_MTR', 'RIPPABILITY', 'SATURATION']
lith[column_order].to_csv('data/rippability.csv', encoding='utf-8', index=False)
