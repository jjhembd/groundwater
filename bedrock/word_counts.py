import pandas
import re
from collections import Counter

# Load the pre-cleaned lithology descriptions
lith = pandas.read_csv('data/cleaned_lith.csv')

# Discard non-string descriptions (NaN)
lith_str = lith[lith['LITHO_MTR'].apply(lambda x: isinstance(x, str))]['LITHO_MTR']

# Split words
words = lith_str.apply(lambda x: re.split(r'[ /&,;\-()+]+', x))

# Flatten to a 1D list of words
wordlist = []
for desc in words: wordlist.extend(desc)

# Count the number of occurences of each word
counts = Counter(wordlist)
wc_df = pandas.DataFrame \
    .from_dict(counts, orient='index') \
    .reset_index() \
    .rename(columns={'index':'word', 0:'count'}) \
    .sort_values('count', ascending=False)

print("Number of distinct words: " + str(wc_df.shape[0]))

# Write out results
col_order = ['count', 'word']
wc_df[col_order].to_csv('data/wordcounts.csv', encoding='utf-8', index=False)
