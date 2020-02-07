# Fix common mis-spellings
def fix(word):
    # Grain size words
    if word in ['samll', 'sml', 'sm']:
        word = 'small'
    elif word in ['fien', 'fein', 'fin', 'fiine', 'finr', 'finre', 'fne']:
        word = 'fine'
    elif word in ['vf']:
        word = 'very fine'
    elif word in ['med', 'med.', 'meduim', 'mediu', 'meidum']:
        word = 'medium'
    elif word in ['larg', 'lrg', 'lge', 'lg', 'lg.']:
        word = 'large'
    elif word in ['caorse', 'coars', 'coase', 'course', 'coaurse', 'couarse', 'corase', 'corse', 'crse']:
        word = 'coarse'
    elif word in ['bolders']:
        word = 'boulders'
    elif word in ['gravely']:
        word = 'gravelly'

    # Color words
    elif word in ['ligth', 'lite', 'lt.', 'lt']:
        word = 'light'
    elif word in ['wht', 'whtie', 'wgite']:
        word = 'white'
    elif word in ['darl', 'drak', 'drk.', 'drk', 'dk.', 'dk']:
        word = 'dark'
    elif word in ['balck', 'blakc', 'blk']:
        word = 'black'
    elif word in ['grey', 'gary', 'gry', 'gr', 'gy', 'gay', 'rey']:
        word = 'gray'
    elif word in ['greyish']:
        word = 'grayish'
    elif word in ['liv']:
        word = 'liver'
    elif word in ['rd']:
        word = 'red'
    elif word in ['redish', 'redish.', 'reddist', 'redsih', 'rdish']:
        word = 'reddish'
    elif word in ['pnk']:
        word = 'pink'
    elif word in ['tanish']:
        word = 'tannish'
    elif word in ['brwn', 'bronw', 'brow', 'brwon', 'bown', 'bornw', 'borwn', 'brn', 'brn.', 'br.', 'br', 'vrown']:
        word = 'brown'
    elif word in ['bl', 'bleu', 'bule']:
        word = 'blue'
    elif word in ['grn']:
        word = 'green'
    elif word in ['grensih']:
        word = 'greenish'
    elif word in ['yel', 'yell', 'yello']:
        word = 'yellow'
    elif word in ['yellowis']:
        word = 'yellowish'

    # Surface materials
    elif word in ['urface', 'surf', 'surfae']:
        word = 'surface'
    elif word in ['ashphault', 'asphault']:
        word = 'asphalt'
    elif word in ['aggergate']:
        word = 'aggregate'
    elif word in ['cocncrete', 'conrete', 'concret']:
        word = 'concrete'
    elif word in ['ropsoil', 'topaoil', 'topsoi;', 'topsil', 'opsoil', 'topsoils', 'tosoil']:
        word = 'topsoil'
    elif word in ['lome', 'loma', 'laom', 'loom', 'loan']:
        word = 'loam'
    elif word in ['siol', 'soi;']:
        word = 'soil'
    elif word in ['subsiol', 'subsoi;']:
        word = 'subsoil'
    elif word in ['oberburden', 'obverburden', 'overbirden', 'overbuden', 'overburde', 'overburdon', 'overdurden', 'ovrburden']:
        word ='overburden'

    # Unconsolidated
    elif word in ['caly', 'clat', 'clau', 'clayy', 'ckay', 'c;ay', 'cl;ay', 'clay.', 'cly', 'cvlay', 'cy']:
        word = 'clay'
    elif word in ['clayee', 'clayeye', 'claey']:
        word = 'clayey'
    elif word in ['asnd', 'saand', 'sadn', 'snd', 'samd', 'sans', 'snad', 'sabd', 'sandd', 'sand.', 'sd', 'sd.']:
        word = 'sand'
    elif word in ['quicksnad']:
        word = 'quicksand'
    elif word in ['andy', 'sabdy', 'samdy', 'sandt', 'sandu', 'sany', 'snady', 'sndy', 'sdy', 'sdy.']:
        word = 'sandy'
    elif word in ['silicia']:
        word = 'silica'
    elif word in ['silt.']:
        word = 'silt'
    elif word in ['sillty', 'sitly', 'sity', 'silthy', 'sility', 'slty']:
        word = 'silty'
    elif word in ['liem']:
        word = 'lime'
    elif word in ['limy']:
        word = 'limey'
    elif word in ['gavel', 'grav', 'grave', 'gravle', 'grael', 'gravil', 'grvel', 'grvl', 'grv', 'ravel']:
        word = 'gravel'
    elif word in ['benetonit']:
        word = 'bentonite'

    # Rocks
    elif word in ['andstone', 'sabdstone', 'sadstone', 'samdstone', 'sandst', 'sandsto', 'sandsstone', 'sandstne', 'sandston', 'sandsotne', 'sandstonee', 'sandstone.', 'sandstonre', 'sadnstone', 'sandstoen', 'sanstone', 'sandtone', 'sandstoe', 'sandsone', 'snadstone', 'sndstone', 'sndstne', 'sndstn', 'sndst', 's.s.', 'ss']:
        word = 'sandstone'
    elif word in ['ssst', 'ssst.']:
        word = 'sandstone streaks'
    elif word in ['androck', 'sabdrock', 'sandrcok', 'sandrok', 'sandrk', 'sandsrock', 'sandroack', 'sandrpck', 'sandrockk', 'sandorck', 'samdrock', 'sandrocl', 'sandrocj', 'snadrock', 'sadnrock', 'sandrokc', 'sandock', 'sanrock', 'sndrock', 'sndrck', 'sndrk']:
        word = 'sandrock'
    elif word in ['silstone', 'siltone', 'siltsone', 'sitlstone']:
        word = 'siltstone'
    elif word in ['dhale', 'sgake', 'shake', 'shal', 'sjale', 'sha;e', 'sja;e', 'shal;e', 'shjale', 'shlale', 'sghale', 'sgale', 'shall', 'shaell', 'shail', 'shael', 'sale', 'shalee', 'shalr', 'sahel', 'shlae', 'sahle', 'shalke', 'shalw', 'shle', 'sh', 'sh.']:
        word = 'shale'
    elif word in ['shaly', 'shy']:
        word = 'shaley'
    elif word in ['shst', 'shst.']:
        word = 'shale streaks'
    elif word in ['calcihe', 'caleche', 'calichie', 'calachie', 'calache', 'calichi', 'calicho', 'cal', 'clachie', 'cleachy', 'cleache', 'cleatche', 'clechie', 'cleche', 'cliche', 'colechy', 'colychee', 'colichie', 'cleachie', 'claiche', 'calechi', 'calechie']:
        word = 'caliche'
    elif word in ['chaulk']:
        word = 'chalk'
    elif word in ['limesstone', 'limetone', 'limestnone', 'limeston', 'limestoen', 'limstone', 'l.s.']:
        word = 'limestone'
    elif word in ['annihydrite']:
        word = 'anhydrite'
    elif word in ['stowe', 'stne', 'stn']:
        word = 'stone'
    elif word in ['rcok', 'rokc', 'rck']:
        word = 'rock'
    elif word in ['dolamite', 'dolermite', 'dolimite', 'dolo']:
        word = 'dolomite'
    elif word in ['gyp', 'gyp.', 'gypsium', 'gypsom', 'gypson', 'gip', 'gipp', 'jip', 'jepson']:
        word = 'gypsum'
    elif word in ['churt', 'chirt']:
        word = 'chert'
    elif word in ['garnite', 'granit', 'grainte', 'grante']:
        word = 'granite'
    elif word in ['flinet']:
        word = 'flint'
    elif word in ['conglomarate', 'conglomarte', 'conglomrate', 'congiomarte', 'cong.']:
        word = 'conglomerate'

    # Concentration words
    elif word in ['steaks', 'strks', 'strks.', 'stks', 'stks.', 'strk', 'str.', 'str', 'stk']:
        word = 'streaks'
    elif word in ['innerbedded']:
        word = 'interbedded'
    elif word in ['stirps', 'strps', 'tirps', 'trips']:
        word = 'strips'
    elif word in ['stirp']:
        word = 'strip'
    elif word in ['occ', 'occ.']:
        word = 'occasional'

    # Strength words
    elif word in ['ahrd', 'hard.', 'hd', 'hd.']:
        word = 'hard'
    elif word in ['hdst', 'hdst.']:
        word = 'hard streaks'
    elif word in ['weatherd']:
        word = 'weathered'
    elif word in ['porus']:
        word = 'porous'
    elif word in ['borken', 'broekn', 'brokwn']:
        word = 'broken'
    elif word in ['bloe']:
        word = 'blow'
    elif word in ['aluvial']:
        word = 'alluvial'
    elif word in ['loose.', 'loos', 'losoe']:
        word = 'loose'

    # Wetness words
    elif word in ['wtrsnd', 'wtrsnad', 'wtrsand', 'wtersand', 'waterand', 'watersamd', 'watersadn', 'watersnd', 'watersnad', 'watersabd', 'watrsand', 'watesand']:
        word = 'watersand'
    elif word in ['saturated.']:
        word = 'saturated'
    elif word in ['slopy']:
        word = 'sloppy'
    elif word in ['muckie']:
        word = 'mucky'
    elif word in ['damp.']:
        word = 'damp'
    elif word in ['mois', 'moist.']:
        word = 'moist'
    elif word in ['moisture.']:
        word = 'moisture'
    elif word in ['dry.']:
        word = 'dry'
    elif word in ['wtr', 'wtr.', 'wter']:
        word = 'water'
    elif word in ['aquifier']:
        word = 'aquifer'

    # Other
    elif word in ['vy']:
        word = 'very'
    elif word in ['fialry', 'fiarly', 'failry', 'farily']:
        word = 'fairly'
    elif word in ['sligtly']:
        word = 'slightly'
    elif word in ['iwth']:
        word = 'with'
    elif word in ['unkown', 'unknonw', 'ukwn']:
        word = 'unknown'
    elif word in ['crystalized', 'crytalized']:
        word = 'crystallized'
    elif word in ['granualr']:
        word = 'granular'
    elif word in ['qiuck', 'qucik']:
        word = 'quick'
    elif word in ['crevis', 'grevice']:
        word = 'crevice'
    elif word in ['ned', 'hed']:
        word = 'bed'
    elif word in ['lith', 'lith.', 'lithology.']:
        word = 'lithology'
    elif word in ['obtained.']:
        word = 'obtained'
    elif word in ['avail', 'avail.', 'available.']:
        word = 'available'
    elif word in ['non', 'n0ne', 'none.']:
        word = 'none'

    # Specific formations
    elif word in ['rushsprgs', 'rushspgs', 'rshspgs']:
        word = 'rush springs'
    elif word in ['rsh']:
        word = 'rush'
    elif word in ['sprgs', 'sprg', 'spgs', 'spgs.']:
        word = 'springs'

    return word
