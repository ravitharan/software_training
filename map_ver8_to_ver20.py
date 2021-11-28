import re
import sys

CONFIG_VER20_TEMPLATE = "scripts/config_ver20_template.txt"

PATTERN_STRUCTURE   = re.compile(r'^(\w+):')

def get_structure(config_file):
    params      = {}
    with open(config_file) as file_in:
        members     = []
        structure   = None
        for line in file_in:
            match_structure = PATTERN_STRUCTURE.match(line)
            if match_structure:
                if structure:
                    params[structure] = members
                structure = match_structure.group(1)
                members = []
            else:
                values = line.strip().split()
                if len(values) == 3:
                    members.append((values[0], values[2]))
                elif len(values) == 1:
                    members.append([values[0], None])
        if structure:
            params[structure] = members

    return params

def get_all_matches(params_list, search_key, param_name):
    matching_keys = {
        "PL_FAULT_LIMIT"    : "PL_fl",
        "PL_FAULT_MASK"     : "PL_fm",
        "R5_FAULT_LIMIT"    : "r5_fl",
        "R5_FAULT_MASK"     : "r5_fm",
        }
    found_match = []
    for key in params_list:
        for item in params_list[key]:
            if item[0] == param_name:
                found_match.append((key, item[0], item[1]))

    if (len(found_match) > 1) and (search_key in matching_keys):
        needed_key = matching_keys[search_key]
        filtered_match = [ x for x in found_match if x[0] == needed_key ]
        found_match = filtered_match

    return found_match


if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print(f'Argument error\n Usage: {sys.argv[0]} <config_ver8_file>')
        exit(1)
    params_ver8 = get_structure(sys.argv[1])
    params_ver20 = get_structure(CONFIG_VER20_TEMPLATE)

    for key in params_ver20:
        for i, item in enumerate(params_ver20[key]):
            matches = get_all_matches(params_ver8, key, item[0])
            if len(matches) == 1:
                params_ver20[key][i][1] = matches[0][2]
            elif len(matches) > 1:
                matching_values = "SELECT_ONE: "
                for match in matches:
                    matching_values += f' {match[0]}.{match[1]} = {match[2]}'
                params_ver20[key][i][1] = matching_values

    for key in params_ver20:
        print(f'\n{key}:')
        for item in params_ver20[key]:
            if item[1]:
                print(f'  {item[0]:48} = {item[1]}')
            else:
                print(f'  {item[0]:48} = ')
