import re

ver20_file = open("config_ver20.txt","r")
ver20_file_template = open("config_ver20_template.txt","r")
ver_file = open("config_ver.txt","w")
name_dict = {"PL_fl:":"PL_FAULT_LIMIT:","PL_fm:":"PL_FALUT_MASK:","r5_fl:":"R5_FAULT_LIMIT:","r5_fm:":"R5_FAULT_MASK:"}

def version8_file_data(ver8_file):
    """
    ver8_data_dict = {'MGU:': [['res_mech_offset_in_u16', '52360'], ['Ld', '9.000e-05'], ['Lq', '7.000e-05']],...}
    
    """
    ver8_file = open("config_ver8.txt", "r")
    ver8_lines = ver8_file.readlines()

    ver8_data_dict = {}
    for line in ver8_lines:
        
        if ":" in line:
            line = line.strip().replace('\n', '')
            key = line
            ver8_data_list = []    
        else: 
            line = re.sub(" +","",line)
            line = line.split("=")
            if len(line) == 2:  
                line[1] = line[1].strip().replace('\n', '')
                ver8_data_list.append(line)
                ver8_data_dict[key] = ver8_data_list
                             
    ver8_file.close()
    
    #print(ver8_data_dict)
    return ver8_data_dict

ver8_data_dict = version8_file_data(ver8_file)

def version20_file_data(ver20_file):
    """
    ver20_data_dict = {'IDENTITY:': ['config_version', 'mgu_id', 'inv_id', ''], 'RSLV_OFFSETS:': ['mgu_1', 'mgu_2', 'mgu_3', 'mgu_4', 'mgu_5'],..}
    
    """
    
    ver20_lines = ver20_file.readlines() 

    ver20_data_dict = {}
    for ver20_line in ver20_lines:
        if ":" in ver20_line:
            #ver20_line = re.sub(" +","",ver20_line)
            ver20_line = ver20_line.strip().replace('\n', '')
            key = ver20_line
            ver20_data_list = [] 
        else:
            ver20_line = re.sub(" +","",ver20_line)
            ver20_line = ver20_line.strip().replace('\n', '')
            ver20_data_list.append(ver20_line)
            ver20_data_dict[key] = ver20_data_list
    ver20_file.close()

    #print(ver20_data_dict)
    return ver20_data_dict

ver20_data_dict = version20_file_data(ver20_file)

def value_add_to_list(ver20_data_dict):
    """
    name_value_dict = {'R5_FAULT_LIMIT:': [['Iabc', '9.500e+02'], ['Pdc', '2.500e+05'], ['Idc', '6.000e+02']],...}
    name_value_list = [['Ld', '9.000e-05'], ['Lq', '7.000e-05'], ['phi', '5.663e-02']]

    """
    name_value_dict = {}
    name_value_list = []
    for key in ver8_data_dict:
        for key1 in name_dict:
            if key == key1:
                data_values = []
                for value_list in ver8_data_dict[key]:
                    data = []
                    for value_list2 in ver20_data_dict[name_dict[key1]]:
                        if value_list[0] == value_list2:
                            
                            data.append(value_list2)
                            data.append(value_list[1])
                      
                    data_values.append(data)
                name_value_dict[name_dict[key1]] = data_values
            else:
                for value_list in ver20_data_dict:
                    for value in ver20_data_dict[value_list]:
                        data = []
                        for key_value in ver8_data_dict[key]:
                            if value == key_value[0]:
                                data.append(value)
                                data.append(key_value[1])
                                name_value_list.append(data)
                 
    #print(name_value_list)
    return name_value_dict,name_value_list

name_value_dict,name_value_list = value_add_to_list(ver20_data_dict)

def text_file_write(ver_file):
    """
        New text file write
            IDENTITY:
              config_version			=   8
              mgu_id				=   6
              inv_id				=   6

    """
    ver20_file = open("config_ver20.txt","r")
    ver20_lines = ver20_file.readlines()
    template_lines = ver20_file_template.readlines()
    for ver_line, temp_line in zip(ver20_lines,template_lines):
        ver_line = re.sub(" +","",ver_line)
        ver_line = ver_line.strip().replace('\n', '')   
        temp_line = temp_line.strip().replace('\n', '')
        count = 0
        for key in name_dict:
            if count == 0: 
                if ver_line != name_dict[key]:
                    if ":" in ver_line:
                        ver_file.write(temp_line)
                        ver_file.write('\n')
                        break
                    else:
                        for list_value in name_value_list: 
                            if list_value[0] == ver_line:
                                ver_file.write("  ")
                                ver_file.write(temp_line)
                                ver_file.write("   ")
                                ver_file.write(list_value[1])
                                ver_file.write('\n')
                                count += 1
                                break
                        else:
                            ver_file.write("  ")
                            ver_file.write(temp_line)
                            ver_file.write('\n')
                            count += 1
                            break
                else:
                    if ver_line == name_dict[key]:
                        ver_file.write(temp_line)
                        ver_file.write('\n')
                        name = ver_line                
                        count += 1
                    else:
                        for list_value2 in name_value_dict[name]:
                            if ver_line == list_value2[0]:
                                ver_file.write("  ")
                                ver_file.write(temp_line)
                                ver_file.write("   ")
                                ver_file.write(list_value2[1])
                                ver_file.write('\n')
                                count += 1
    ver20_file.close()
    ver_file.close()

    return ver20_lines

ver20_lines = text_file_write(ver_file)
