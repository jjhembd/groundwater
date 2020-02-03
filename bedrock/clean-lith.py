import pandas
from description import fixdescription

# Get raw file, report statistics
lith = pandas.read_csv('data/WL_Lithology.csv')
numvals = lith['LITHO_MTR'].value_counts().shape[0]
print('Number of descriptions in raw file: ' + str(numvals))

# Fix spelling and other problems
lith['LITHO_MTR'] = lith['LITHO_MTR'].map(fixdescription, na_action='ignore')
numvals = lith['LITHO_MTR'].value_counts().shape[0]
print('After fixing common mis-spellings: ' + str(numvals))

# Write out to a new file
column_order = ['SITE_ID', 'LITHO_MTR', 'LITHO_TOP', 'LITHO_BOT', 'SATURATION']
lith[column_order].to_csv('data/cleaned_lith.csv', encoding='utf-8', index=False, float_format='%d')
