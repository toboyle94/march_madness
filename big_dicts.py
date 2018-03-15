"""
Helpful data structures for March Madness hacking
"""

# dictionary - team : id
team_ids = { 
    'UVA' : 258, 
    'UMBC' : 2378, 
    'CREI' : 156,
    'KSU' : 2306,
    'UK' : 96,
    'DAV' : 2166,
    'ARIZ' : 12,
    'BUFF' : 2084,
    'MIA' : 2390,
    'L-IL' : 2350,
    'TENN' : 2633,
    'WRST' : 2750,
    'NEV': 2440,
    'TEX' : 251,
    'CIN' : 2132,
    'GAST' : 2247,
    'XAV': 2752,
    'NCCU' : 2428,
    'TXSO' : 2640,
    'MIZ' : 142,
    'FSU' : 52,
    'OSU' : 194,
    'SDST' : 2571,
    'GONZ' : 2250,
    'UNCG' : 2430,
    'HOU' : 248,
    'SDSU' : 21,
    'MICH': 130,
    'MONT' : 149,
    'TAMU' : 245,
    'PROV' : 2507,
    'UNC' : 153,
    'LIP' : 288,
    'VILL' : 222,
    'LIU' : 2341,
    'RAD' : 2515,
    'VT' : 259,
    'ALA' : 333,
    'WVU' : 277,
    'MURR' : 93,
    'WICH' : 2724,
    'MRSH' : 276,
    'FLA' : 57,
    'SBON' : 179,
    'UCLA' : 26,
    'TTU' : 2641,
    'SFA' : 2617,
    'ARK' : 8,
    'BUT' : 2086,
    'PUR' : 2509,
    'CSF' : 2239,
    'KU' : 2305,
    'PENN' : 219,
    'HALL' : 2550,
    'NCST' : 152,
    'CLEM' : 228,
    'NMSU' : 166,
    'AUB' : 2,
    'COFC' : 232,
    'TCU' : 2628,
    'ASU' : 9,
    'SYR' : 183,
    'MSU' : 127,
    'BUCK' : 2083,
    'URI' : 227,
    'OKLA' : 201,
    'DUKE' : 150,
    'IONA' : 314
}

# dictionary - abbreviated name : full name
team_names = { 
    'UVA' : 'Virginia Cavaliers', 
    'UMBC' : 'UMBC Retrievers', 
    'CREI' : 'Creighton Bluejays',
    'KSU' : 'Kansas State Wildcats',
    'UK' : 'Kentucky Wildcats',
    'DAV' : 'Davidson Wildcats',
    'ARIZ' : 'Arizona Wildcats',
    'BUFF' : 'Buffalo Bulls',
    'MIA' : 'Miami Hurricanes',
    'L-IL' : 'Loyola Chicago',
    'TENN' : 'Tennessee Volunteers',
    'WRST' : 'Wright State Raiders',
    'NEV': 'Nevada Wolf Pack',
    'TEX' : 'Texas Longhorns',
    'CIN' : 'Cincinnati Bearcats',
    'GAST' : 'Georgia State Panthers',
    'XAV': 'Xavier Musketeers',
    'NCCU' : 'North Carolina Central Eagles',
    'TXSO' : 'Texas Southern Tigers',
    'MIZ' : 'Missouri Tigers',
    'FSU' : 'Florida State Seminoles',
    'OSU' : 'Ohio State Buckeyes',
    'SDST' : 'South Dakota State Jackrabbits',
    'GONZ' : 'Gonzago Bulldogs',
    'UNCG' : 'UNC Greensboro Spartans',
    'HOU' : 'Houston Cougars',
    'SDSU' : 'San Diego State Aztecs',
    'MICH': 'Michigan Wolverines',
    'MONT' : 'Montana Grizzlies',
    'TAMU' : 'Texas A&M Aggies',
    'PROV' : 'Providence Friars',
    'UNC' : 'North Carolina Tar Heels',
    'LIP' : 'Lipscomb Bisons',
    'VILL' : 'Villanova Wildcats',
    'LIU' : 'LIU Brooklyn Blackbirds',
    'RAD' : 'Radford Highlanders',
    'VT' : 'Virginia Tech Hokies',
    'ALA' : 'Alabama Crimson Tide',
    'WVU' : 'West Virginia Mountaineers',
    'MURR' : 'Murray State Racers',
    'WICH' : 'Wichita State Shockers',
    'MRSH' : 'Marshall Thundering Herd',
    'FLA' : 'Florida Gators',
    'SBON' : 'Bonaventure Bonnies',
    'UCLA' : 'UCLA Bruins',
    'TTU' : 'Texas Tech Red Raiders',
    'SFA' : 'Stephen F. Austin Lumberjacks',
    'ARK' : 'Arkansas Razorbacks',
    'BUT' : 'Butler Bulldogs',
    'PUR' : 'Purdue Boilermakers',
    'CSF' : 'CS Fullerton Titans',
    'KU' : 'Kansas Jayhawks',
    'PENN' : 'Pennsylvania Quakers',
    'HALL' : 'Seton Hall Pirates',
    'NCST' : 'NC State Wolfpack',
    'CLEM' : 'Clemson Tigers',
    'NMSU' : 'New Mexico State Aggies',
    'AUB' : 'Auburn Tigers',
    'COFC' : 'Charleston Cougars',
    'TCU' : 'TCU Horned Frogs',
    'ASU' : 'Arizon State Sun Devils',
    'SYR' : 'Syracuse Orange',
    'MSU' : 'Michigan State Spartans',
    'BUCK' : 'Bucknell Bison',
    'URI' : 'Rhode Island Rams',
    'OKLA' : 'Oklahoma Sooners',
    'DUKE' : 'Duke Blue Devils',
    'IONA' : 'Iona Gaels'
}

# don't know if this is helpful, but a list of tuples representing 1st round matchups (play-in games are nested tuples)
round_1 =  [('UVA', 'UMBC'), ('CREI', 'KSU'),
            ('UK', 'DAV'), ('ARIZ', 'BUFF'),
            ('MIA', 'L-IL'), ('TENN', 'WRST'),
            ('NEV', 'TEX'), ('CIN', 'GAST'),

            ('XAV', 'TXSO'), ('MIZ', 'FSU'),
            ('OSU', 'SDST'), ('GONZ', 'UNCG'),
            ('HOU', 'SDSU'), ('MICH', 'MONT'),
            ('TAMU', 'PROV'), ('UNC', 'LIP'),

            ('VILL', 'RAD'), ('VT', 'ALA'),
            ('WVU', 'MURR'), ('WICH', 'MRSH'),
            ('FLA', 'SBON'), ('TTU', 'SFA'),
            ('ARK', 'BUT'), ('PUR', 'CSF'), 
            
            ('KU', 'PENN'), ('HALL', 'NCST'),
            ('CLEM', 'NMSU'), ('AUB', 'COFC'),
            ('TCU', 'SYR'), ('MSU', 'BUCK'),
            ('URI', 'OKLA'), ('DUKE', 'IONA')]
