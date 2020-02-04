import re
from spelling import fixspelling

def fixdescription(description):
    # BEWARE: description must not be a NaN!
    lc_desc = description.lower()

    if lc_desc in ['ob', 'o b', 'o-b', 'o - b', 'ovbd', '0b']:
        return 'overburden'
    if lc_desc in ['to soil', 'op soil', 'top sil', 'tops oil', 'tops soil', 'top s0il']:
        return 'topsoil'
    if lc_desc in ['r b']:
        return 'redbed'
    if lc_desc in ['na', 'not avail.', 'not available', 'n0ne', 'non', 'none', 'none.', 'none obtained', 'none provided', 'no data obtained', 'no data', 'nd', 'not described', 'not logged', 'not reported', 'no lith obtained', 'no lithology', 'no lithology provided', 'no log', 'no logs taken', 'no lith avail.', 'no samples', 'no sample taken', 'unavailable']:
        return 'INVALID'

    # Replace 'w/' abbreviations by 'with'. 
    # Note: We do not expect 'with' at the start or end of the description 
    # Hence the negative lookbehind (?!^) and lookahead (?!$)
    desc = re.sub(r'(?!^) w/ ?(?!$)', ' with ', lc_desc)

    # Split words, keeping the separators (', ', '/', etc.) in the list
    words = re.split(r'([ /&,\-]+)', desc)

    fixedwords = [fixword(w) for w in words]

    # Discard separators at beginning or end of description
    separators = [' ', ' & ', ' / ', ', ', ' - ']
    if fixedwords[0] in separators: del fixedwords[0]
    last = len(fixedwords) - 1
    if fixedwords[last] in separators: del fixedwords[last]

    compoundedwords = compoundwords(fixedwords)
    return ''.join(compoundedwords)

def fixword(word):
    # Fix and return any word separator strings
    if re.fullmatch(r' +', word): return ' '
    if re.fullmatch(r' *& *', word): return ' & '
    if re.fullmatch(r' */ *', word): return ' / '
    if re.fullmatch(r' *, *', word): return ', '
    if re.fullmatch(r' *- *', word): return ' - '
    
    # TODO: Don't substitute & if this is the first word (e.g., 'and stone')
    if word == 'and': return '&'

    return fixspelling(word)

def compoundwords(words):
    compounds = ['sandstone', 'sandrock', 'watersand', 'quicksand',
            'limestone', 'siltstone', 'claystone', 'redbed', 'redbeds',
            'topsoil', 'subsoil', 'bedrock']
    i = 0
    while i < len(words) - 2:
        separator = words[i + 1]
        compound = words[i] + words[i + 2]
        if separator == ' ' and compound in compounds:
            words[i] = compound
            del words[i + 1:i + 3] # Deletes indices i + 1 and i + 2, NOT i + 3
        i += 1
            
    return words
