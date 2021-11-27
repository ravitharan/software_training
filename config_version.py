def fetch_data(file_name):
    """
    Parsing data from config file into a dictionary
    input : config_ver8 or config_ver20 file
    output: {MGU:[ [Ld, 9.000e-05], [], [] ] , ......}
    """
    with open(file_name) as fp:
       line = fp.readline()
       cnt = 1
       heading = []
       temp_list  = []
       list_of_list = []
       while line:
           if ":" in line:
               line = line.replace(":" , '').strip()
               heading.append(line)
               if temp_list:
                   list_of_list.append(temp_list)
               temp_list = []
           else:
               if '=' in line:
                   line_list = line.split('=')
                   line_list[0] = line_list[0].strip()
                   line_list[1] = line_list[1].strip()
                   temp_list.append(line_list)
               else:
                   line = line.strip()
                   line_list = line.split()
                   line_list.append(None)
                   if '' != line:
                       temp_list.append(line_list)

           line = fp.readline()
           cnt += 1
    list_of_list.append(temp_list)
    dictionary = {}
    for dictionary_key, value in zip(heading, list_of_list):
        dictionary[dictionary_key] = value
    fp.close()
    return dictionary



def find_dup(config_8):
    """
    find duplicate object from config_8 dictionary
    input : config_8 dictionary  {MGU:[ [Ld, 9.000e-05], [], [] ] , ......}
    output : {'Pdc': 2, 'Iabc': 2, 'Idc': 3, 'Vdc': 3, 'Trq': 2, 'w_shaft_freq': 2}
    """
    config_8_set = set()
    for key in config_8:
        for list1 in config_8[key]:
            config_8_set.add(list1[0])
    dup_set = set()
    dup_dict = {}
    for config in config_8_set:
        total = 0
        for key in config_8:
            for list1 in config_8[key]:
                if config == list1[0]:
                    total += 1
        if total > 1:
            dup_set.add(config)
            dup_dict[config] = total
    return dup_dict
                           


def replace_dictionary_data(config_8, config_20, dup_dict):
    """
    Write config_8 data to config_20 data
    """
    # replace duplicate data
    search = {"PL_FAULT_LIMIT":"PL_fl", "PL_FALUT_MASK":"PL_fm", "R5_FAULT_LIMIT":"r5_fl", "R5_FAULT_MASK":"r5_fm"}
    for key in search:
        for list1 in config_20[key]:
            for list2 in config_8[search[key]]:
                if list1[0] == list2[0]:
                    for dup in dup_dict:
                        if dup == list1[0]:
                            list1[1] = list2[1]
    # replace data
    for key in config_20:
        for key_1 in config_8:
            for list2 in config_20[key]:
                for list1 in config_8[key_1]:
                    if list1[0] == list2[0]:
                        if list2[1] == None:
                            list2[1] = list1[1]
    return config_20


def write_txt(final_config_20):
    """
     Write in a new file final_config_20 data
    """
    with open('config_ver20_new.txt', 'w') as f:
        for key in final_config_20:
            f.write(key + ":" + '\n')
            for list2 in final_config_20[key]:
                if list2[1] != None:
                    f.write("  " + list2[0])
                    space = 35 - len(list2[0])
                    f.write(space * ' ' + "= " + list2[1] + '\n')
                else:
                    f.write("  " + list2[0] + '\n')

config_8 = fetch_data(file_name = 'config_ver8.txt')
config_20 = fetch_data(file_name = 'config_ver20.txt')
dup_dict = find_dup(config_8)
final_config_20 = replace_dictionary_data(config_8, config_20, dup_dict)
write_txt(final_config_20)
