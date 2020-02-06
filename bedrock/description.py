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

    # Replace 'w/' abbreviations by 'with'. 
    # Note: We do not expect 'with' at the start or end of the description 
    # Hence the negative lookbehind (?<!^) and lookahead (?!$)
    desc_wquotes = re.sub(r'(?<!^) w/ ?(?!$)', ' with ', lc_desc)

    # Strip out double quotes, except after digits or decimals 
    # (keep 6" OR 6." for 6 inches)
    desc = re.sub(r'(?<![0-9.])"', '', desc_wquotes)

    # Split words, keeping the separators (', ', '/', etc.) in the list
    words = re.split(r'([ /&,\-]+)', desc)

    fixedwords = [fixword(w) for w in words]

    # Discard separators at beginning or end of description
    separators = [' ', ' & ', ' / ', ', ', ' - ']
    if fixedwords[0] in separators: del fixedwords[0]
    last = len(fixedwords) - 1
    if fixedwords[last] in separators: del fixedwords[last]

    compoundedwords = compoundwords(fixedwords)
    fixed_desc = ''.join(compoundedwords)

    # Discard rows where no lith is available
    if fixed_desc in ['na','not available', 'none', 'none obtained', 'none provided', 'no data obtained', 'no data', 'nd', 'not described', 'not logged', 'not reported', 'no lithology', 'no lithology obtained', 'no lithology collected', 'no lithologies provided', 'no lithology description obtained', 'no lithology provided', 'no lithology available', 'not lithology available', 'no litholgy data', 'lithology not complete', 'lithology not available', 'no log', 'no logs taken', 'no samples', 'no sample taken', 'unavailable']:
        return 'INVALID'
    plug_regex = r'[0-9]* ?\b(overdrill|drilled|drill)\b( out)? (and|&) \b(plugged|plug|grout)\b'
    if re.fullmatch(plug_regex, fixed_desc): return 'INVALID'

    return fixed_desc

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
            'overburden', 'topsoil', 'subsoil', 'bedrock']
    i = 0
    while i < len(words) - 2:
        separator = words[i + 1]
        compound = words[i] + words[i + 2]
        if separator == ' ' and compound in compounds:
            words[i] = compound
            del words[i + 1:i + 3] # Deletes indices i + 1 and i + 2, NOT i + 3
        i += 1
            
    return words
