We have 900k lithology descriptions in OK, 3.8m in TX. That's likely less than
half of the total&mdash;many are still in scanned, handwritten documents.
Note the effort: a busy driller in his coveralls, takes time to clean his
hands, and pick up pencil and paper to note:

"100 - 135 ft.: Red clay with streaks of fine white sand"

And repeat for thousands of drillers, millions of wells...
Note the value: 4.6 million descriptions of the layers under our feet!

How can we review them? We assume the layers extend for some distance--
many entries should be describing the same thing at different locations.
So we load the OK data into a Pandas dataframe, and count the number of 
unique values in the `LITHO_MTR` field:

```
>>> lith['LITHO_MTR'].value_counts()
shale                                                      49319
clay                                                       32337
sandrock                                                   28838
sand                                                       22091
Clay                                                       18247
red clay                                                   18061
red shale                                                  17054
sandstone                                                  15461
...
Name: LITHO_MTR, Length: 118120, dtype: int64
```

That's out of 893,399 rows. So each layer is repeated <9x?
Well, obviously the formatting is not consistent. Note the various
capitalizations... Let's fix that:

```
>>> lith['LITHO_MTR'].str.lower().value_counts()
shale                                                        77336
clay                                                         62100
sandrock                                                     41308
sand                                                         35883
red clay                                                     27628
red shale                                                    27216
sand rock                                                    25877
sandstone                                                    21579
...
Name: LITHO_MTR, Length: 104442, dtype: int64
```

The peak got taller, but the tail isn't much shorter.
Some obvious fixes: fix misspellings, expand abbreviations, standardize
compound words ('sandrock' and 'sand rock' are the same thing).
But these are nontrivial tasks. First we need to separate words. The delimiter
could be a space, multiple spaces, commas, slashes, dashes... And what to do 
with 'w/'?
Then, ideally, we want to put them back together as they were.

Looking deeper, we can see that there are really 5 things being described:
- Material
- Grain size
- Color
- Strength (how solid/crumbly)
- Wetness

Now there is some overlap: for example, the words 'clay', 'silt', 'sand'
are describing different grain sizes, but we assume clay and sand are probably
also different minerals. So by 'Grain size', we mean only words like 'fine',
'medium', 'coarse'--or even the numerical grain sizes given by some drillers.
Also, 'shale' is just lithified 'clay', but we consider them as different
materials rather than the same material with different strengths.
