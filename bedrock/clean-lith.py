import pandas
from description import fixdescription

# Get raw file
lith = pandas.read_csv('data/WL_Lithology.csv')

numvals = lith['LITHO_MTR'].value_counts().shape[0]
print('Number of descriptions in raw file: ' + str(numvals))

# Fix spelling and other problems
lith['LITHO_MTR'] = lith['LITHO_MTR'].map(fixdescription, na_action='ignore')

numvals = lith['LITHO_MTR'].value_counts().shape[0]
print('After fixing common mis-spellings: ' + str(numvals))
