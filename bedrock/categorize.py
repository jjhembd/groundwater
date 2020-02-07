import re
import pandas

cats = pandas.read_csv('categories.csv')
def get_catwords(category):
    return cats.loc[cats['category'] == category]['word'].tolist()
catwords = {
        'material': get_catwords('material'),
        'color': get_catwords('color'),
        'grainsize': get_catwords('grainsize'),
        'strength': get_catwords('strength'),
        'wetness': get_catwords('wetness')
        }

strengths = pandas.read_csv('materials.csv') \
        .set_index('material')['diggability'] \
        .to_dict()

strength_mods = pandas.read_csv('strengths.csv') \
        .set_index('strength')['diggability'] \
        .to_dict()

def findwords(description, category):
    if not isinstance(description, str): return ''

    raw_words = re.split(r'[ /&,;\-()+]+', description)
    found_words = [word for word in raw_words if word in catwords[category]]
    return ','.join(found_words)

nanval = float('NaN')

def diggability(description):
    if not isinstance(description, str): return nanval

    raw_words = re.split(r'[ /&,;\-()+]+', description)
    materials = [word for word in raw_words if word in catwords['material']]
    modifiers = [word for word in raw_words if word in catwords['strength']]

    # Average the strength ratings of all the materials
    diggabilities = [strengths[mat] for mat in materials if strengths[mat] > 0]
    if len(diggabilities) < 1: return nanval
    diggability = round(sum(diggabilities) / len(diggabilities), 2)

    # Add correction factors for strength modifier words (hard, broken, etc)
    diggability += sum([strength_mods[mod] for mod in modifiers])

    return min(max(1, diggability), 4)
