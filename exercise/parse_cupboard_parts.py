import re

def split_parts_details(parts_description):
    '''
    This will split a parts description (column D value) into [[count1, size1, name1], [count2, size2, name2], ...]
    Input string should have been cleaned
    eg '[2] 9 7/8 X 26 1/2 DOORS [1] 11 7/8 X 6 15/16 DRAWER [1] 11 7/8 X 8 15/16 DRAWER [1] 11 7/8 X 10 7/16 DRAWER [2] 2 X 32 SOLID WOOD [4] 2 X 2 X 32 SOLID WOOD LEG'
    Above description become 
        [
            [2, '9 7/8 X 26 1/2', 'DOORS'],
            [1, '11 7/8 X 6 15/16', 'DRAWER'],
            [1, '11 7/8 X 8 15/16', 'DRAWER'],
            [1, '11 7/8 X 10 7/16', 'DRAWER'],
            [2, '2 X 32', 'SOLID WOOD'],
            [4, '2 X 2 X 32', 'SOLID WOOD LEG']
        ]

    '''
    # Make sure parts_description contain at least one [n]
    if not re.compile('\[\d+\]').search(parts_description):
        print(f'INVALID parts: {parts_description}')
        return []

    # Split string by count ('[n]') entries
    part_entries = re.compile('(\[\d+\])').split(parts_description)
    while '' in part_entries:               # Remove blank entry
        part_entries.remove('')

    parts = []

    for i in range(0, len(part_entries), 2):
        count = int(part_entries[i][1:-1])    # get the number by skipping [ & ]
        size_name = part_entries[i+1]
        # Split string into size and name ('DOOR') entries
        size_name_entries = re.compile('([a-wyzA-WYZ].+)').split(size_name)
        while '' in size_name_entries:               # Remove blank entry
            size_name_entries.remove('')
        parts.append([count, size_name_entries[0].strip(), size_name_entries[1].strip()])

    return parts

description = '[2] 9 7/8 X 26 1/2 DOORS [1] 11 7/8 X 6 15/16 DRAWER [1] 11 7/8 X 8 15/16 DRAWER [1] 11 7/8 X 10 7/16 DRAWER [2] 2 X 32 SOLID WOOD [4] 2 X 2 X 32 SOLID WOOD LEG [GLASS]'
parts = split_parts_details(description)
for part in parts:
    print(part)

