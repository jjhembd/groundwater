# Fix common mis-spellings
def fixspelling(word):
    # Grain size words
    if word in ['sml']:
        word = 'small'
    elif word in ['fien', 'fein']:
        word = 'fine'
    elif word in ['med', 'med.', 'meduim', 'mediu']:
        word = 'medium'
    elif word in ['lrg', 'lge', 'lg', 'lg.']:
        word = 'large'
    elif word in ['course', 'couarse', 'corse']:
        word = 'coarse'
    elif word in ['gravely']:
        word = 'gravelly'
    # TODO: Smarter handling for dashes
    elif word in ['fine-med', 'fine-med.']:
        word = 'fine-medium'
    elif word in ['med-lg', 'med-lg.']:
        word = 'medium-large'

    # Color words
    elif word in ['lite', 'lt.']:
        word = 'light'
    elif word in ['wht', 'whtie', 'wgite']:
        word = 'white'
    elif word in ['darl', 'drk', 'dk.', 'dk']:
        word = 'dark'
    elif word in ['blakc', 'blk']:
        word = 'black'
    elif word in ['grey', 'gary', 'gry', 'gr', 'gy', 'gay']:
        word = 'gray'
    elif word in ['rd']:
        word = 'red'
    elif word in ['redish', 'reddist']:
        word = 'reddish'
    elif word in ['pnk']:
        word = 'pink'
    elif word in ['brwn', 'brwon', 'bown', 'brn', 'brn.', 'br.', 'br']:
        word = 'brown'
    elif word in ['bl', 'bule']:
        word = 'blue'
    elif word in ['grn']:
        word = 'green'
    elif word in ['yellowis']:
        word = 'yellowish'

    # Surface materials
    elif word in ['urface']:
        word = 'surface'
    elif word in ['ashphault', 'asphault']:
        word = 'asphalt'
    elif word in ['aggergate']:
        word = 'aggregate'
    elif word in ['cocncrete']:
        word = 'concrete'
    elif word in ['topsoi;', 'topsil', 'opsoil', 'topsoils']:
        word = 'topsoil'
    elif word in ['lome', 'loma', 'laom', 'loom', 'loan']:
        word = 'loam'
    elif word in ['soi;']:
        word = 'soil'
    elif word in ['subsiol', 'subsoi;']:
        word = 'subsoil'
    elif word in ['oberburden', 'overbirden', 'overbuden', 'overburdon', 'overdurden']:
        word ='overburden'

    # Unconsolidated
    elif word in ['caly', 'clau', 'clayy', 'ckay', 'c;ay', 'cl;ay', 'clay.', 'cly', 'cvlay', 'cy']:
        word = 'clay'
    elif word in ['clayee']:
        word = 'clayey'
    elif word in ['saand', 'sadn', 'snd', 'samd', 'snad', 'sabd', 'sandd', 'sand.']:
        word = 'sand'
    elif word in ['sandu', 'snady', 'sndy', 'sdy']:
        word = 'sandy'
    elif word in ['silicia']:
        word = 'silica'
    elif word in ['silt.']:
        word = 'silt'
    elif word in ['sillty', 'sitly', 'sity', 'silthy']:
        word = 'silty'
    elif word in ['liem']:
        word = 'lime'
    elif word in ['limy']:
        word = 'limey'
    elif word in ['grav', 'gravle', 'grael', 'grvl', 'ravel']:
        word = 'gravel'
    elif word in ['benetonit']:
        word = 'bentonite'

    # Rocks
    elif word in ['sabdstone', 'sandsstone', 'sandston', 'sandsotne', 'sandstonee', 'sandstonre', 'sadnstone', 'sandstoen', 'sanstone', 'sandtone', 'sandstoe', 'sandsone', 'sndstone', 'sndstne', 'sndst', 's.s.']:
        word = 'sandstone'
    elif word in ['androck', 'sabdrock', 'sandrok', 'sandsrock', 'sandroack', 'sandrpck', 'sandrockk', 'sandorck', 'samdrock', 'sandrocl', 'sandrocj', 'snadrock', 'sadnrock', 'sandrokc', 'sandock', 'sanrock', 'sndrock', 'sndrck', 'sndrk']:
        word = 'sandrock'
    elif word in ['silstone', 'siltone']:
        word = 'siltstone'
    elif word in ['sjale', 'sja;e', 'shjale', 'sghale', 'sgale', 'shall', 'shail', 'shael', 'sale', 'shalee', 'sahel', 'shlae', 'sahle', 'shalke', 'shle', 'sh']:
        word = 'shale'
    elif word in ['caleche', 'calichie', 'calachie', 'calache', 'calichi', 'calicho', 'cal', 'cleachy', 'cleache', 'clechie', 'cliche', 'colechy', 'colychee', 'cleachie', 'claiche', 'calechi', 'calechie']:
        word = 'caliche'
    elif word in ['chaulk']:
        word = 'chalk'
    elif word in ['limesstone', 'limetone', 'limestnone', 'limeston', 'limestoen', 'limstone', 'l.s.']:
        word = 'limestone'
    elif word in ['stowe', 'stne', 'stn']:
        word = 'stone'
    elif word in ['rcok', 'rokc', 'rck']:
        word = 'rock'
    elif word in ['dolamite', 'dolermite']:
        word = 'dolomite'
    elif word in ['gyp', 'gyp.', 'gypsom', 'gypson', 'gip', 'gipp', 'jepson']:
        word = 'gypsum'
    elif word in ['churt', 'chirt']:
        word = 'chert'
    elif word in ['granit', 'grainte']:
        word = 'granite'
    elif word in ['flinet']:
        word = 'flint'
    elif word in ['conglomarate', 'conglomarte', 'conglomrate', 'congiomarte', 'cong.']:
        word = 'conglomerate'

    # Concentration words
    elif word in ['strks', 'strks.', 'stks', 'strk']:
        word = 'streaks'
    elif word in ['innerbedded']:
        word = 'interbedded'
    elif word in ['stirps', 'trips']:
        word = 'strips'
    elif word in ['occ', 'occ.']:
        word = 'occasional'

    # Wetness words
    elif word in ['wtrsnd', 'watersamd', 'watersnd', 'watersabd']:
        word = 'watersand'
    elif word in ['saturated.']:
        word = 'saturated'
    elif word in ['slopy']:
        word = 'sloppy'
    elif word in ['wtr', 'wtr.', 'wter']:
        word = 'water'

    # Other
    elif word in ['fiarly', 'failry']:
        word = 'fairly'
    elif word in ['sligtly']:
        word = 'slightly'
    elif word in ['iwth']:
        word = 'with'
    elif word in ['unkown', 'unknonw', 'ukwn']:
        word = 'unknown'
    elif word in ['crystalized']:
        word = 'crystallized'
    elif word in ['granualr']:
        word = 'granular'
    elif word in ['crevis']:
        word = 'crevice'

    return word