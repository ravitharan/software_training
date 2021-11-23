config_ver8 = open('config_ver8.txt', 'r')
Lines = config_ver8.readlines()



""" Fetching and cleaning data from config_8 file into a List of list """
def fetch_data_8(Lines):
    count = 0
    config_8 = []
    for line in Lines:
        count += 1
        if (not ":" in line) and ('=' in line):
                temp_list = line.strip().split("=")
                temp_list[0] = temp_list[0].strip()
                temp_list[1] = temp_list[1].strip()
                config_8.append(temp_list)
    return config_8

config_8 = fetch_data_8(Lines)
config_ver8.close()

""" delete duplicate object from config_8 list """
def del_dup(config_8):
    config_8_set = set()
    for list1 in config_8:
        config_8_set.add(list1[0])
    dup_set = set()
    #dup_dict = {}
    for config in config_8_set:
        total = 0
        for list1 in config_8:
            if config == list1[0]:
                total += 1
        if total > 1:
            dup_set.add(config)
            #dup_dict[config] = total
    #print(dup_dict)
            
    for set_item in dup_set:
        count = 0
        for list1 in config_8:
            if list1[0] == set_item:
                config_8.pop(count)
            count +=1
    return config_8
                
            
config_8 = del_dup(config_8)


""" Fetching and cleaning data from config_20 file into a dictionaryionary """
filepath = 'config_ver20.txt'

def fetch_data_20(filepath):
    with open(filepath) as fp:
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

config_20 = fetch_data_20(filepath = 'config_ver20.txt')


""" Write config_8 data to config_20 data """

def change_dictionary_data(dictionary):
    for list2 in config_8:
        for key in dictionary:
            for value in dictionary[key]:
                if len(value) == 1:
                    if list2[0] == value[0]:
                        value.append(list2[1])
    final_config_20 = dictionary
    return final_config_20

final_config_20 = change_dictionary_data(config_20)
print(final_config_20)
""" Write in a new file final_config_20 data """

def write_txt(final_config_20):
    with open('config_ver20_new.txt', 'w') as f:
        for key in final_config_20:
            f.write(key + ":" + '\n')
            for list2 in final_config_20[key]:
                if len(list2) == 2:
                    f.write("  " + list2[0])
                    space = 35 - len(list2[0])
                    f.write(space* ' ' + "= " + list2[1] + '\n')
                else:
                    f.write("  " + list2[0] + '\n')
        
write_txt(final_config_20)   
