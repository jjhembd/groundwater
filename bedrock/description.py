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
    if lc_desc in ['not avail.', 'none', 'none obtained', 'not reported', 'no lith obtained']:
        return 'INVALID'

    words = lc_desc.split()
    fixedwords = [fixword(w) for w in words]

    compoundedwords = compoundwords(fixedwords)
    return ' '.join(compoundedwords)

def fixword(word):
    if word == '/': return '/'
    if word == 'w/': return 'with'
    # TODO: Don't substitute & if this is the first word (e.g., 'and stone')
    if word == 'and': return '&'

    # Check for 'w/' or '/' prefix
    prefix = ''
    if word[0:2] == 'w/':
        prefix = 'with '
        word = word[2:]
    elif word[0] == '/':
        prefix = '/ '
        word = word[1:]

    # Check for ',' or '/' postfix
    postfix = ''
    if word[-1:] == ',':
        postfix = ','
        word = word[0:-1]
    elif word[-1:] == '/':
        postfix = ' /'
        word = word[0:-1]

    # Check for multiple words joined by slashes
    subwords = word.split('/')

    # Fix spelling of the cleaned words
    fixed_subwords = [fixspelling(sw) for sw in subwords]

    # Re-combine, but add spaces around the slashes
    recombined = ' / '.join(fixed_subwords)

    return prefix + recombined + postfix

def compoundwords(words):
    compounds = ['sandstone', 'sandrock', 'watersand', 'quicksand',
            'limestone', 'siltstone', 'claystone', 'redbed', 'redbeds',
            'topsoil', 'subsoil', 'bedrock']
    i = 0
    while i < len(words) - 1:
        compound = words[i] + words[i + 1]
        if compound in compounds:
            words[i] = compound
            del words[i + 1]
        i += 1
            
    return words
