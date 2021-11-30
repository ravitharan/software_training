import re

def ver8_and_ver20_data(file1,file2):
    """
    {'MGU:': [['res_mech_offset_in_u16', '52360'], ['Ld', '9.000e-05']],...}
    {'IDENTITY:': [['config_version'], ['mgu_id']],...}
    """
    ver8_file = open(file1, "r")
    ver20_file = open(file2,"r")
    ver8_lines = ver8_file.readlines()
    ver20_lines = ver20_file.readlines()

    ver8_data_dict = {}
    ver20_data_dict = {}
    for line in ver8_lines :
        line = line.strip().replace('\n', '')
        line = re.sub(" +","",line)
        if ":" in line :
            key = line
            ver8_data_list = []
        else:
            line = line.split("=")
            ver8_data_list.append(line)
            ver8_data_dict[key] = ver8_data_list
    ver8_file.close()

    for line in ver20_lines :
        line = line.strip().replace('\n', '')
        line = re.sub(" +","",line)
        if ":" in line :
            key = line
            ver20_data_list = []
        else:
            line = line.split()
            ver20_data_list.append(line)
            ver20_data_dict[key] = ver20_data_list
            
    ver20_file.close()
    return ver8_data_dict, ver20_data_dict

def value_add_to_list(ver8_data_dict):
    """
    {'IDENTITY:': [['config_version', '8'], ['mgu_id', '6']],...}
    """
    name_dict = {"PL_fl:":"PL_FAULT_LIMIT:","PL_fm:":"PL_FALUT_MASK:","r5_fl:":"R5_FAULT_LIMIT:","r5_fm:":"R5_FAULT_MASK:"}
    for key in ver20_data_dict:
        for key2 in name_dict:
            if key == name_dict[key2]:
                for value2 in ver20_data_dict[name_dict[key2]]:
                    for value in ver8_data_dict[key2]:
                         
                        if len(value2) != 0 and len(value) != 0 and value2[0] != '' and value[0] != '':
                            if value[0] == value2[0]:
                                 value2.insert(1,value[1])
                                 if len(value2) == 3:
                                     value2.pop(2)
            else:
                for list_value in ver20_data_dict[key]:
                    for list_key in ver8_data_dict:
                        for list_value2 in ver8_data_dict[list_key]:
                                if len(list_value) != 0 and len(list_value2) != 0 :
                                    if list_value[0] == list_value2[0]:
                                        if len(list_value) == 1 :
                                            list_value.append(list_value2[1])
    return ver20_data_dict

def version_file_write(ver20_data_dict):
    """
    Config8_ver data to config_version file write
    """
    version_file = open("config_version.txt","w")  
    for key in ver20_data_dict:
        if ":" in key:
            version_file.write(key)
            version_file.write('\n')    
            for value in ver20_data_dict[key]:
                if len(value) == 1:
                    version_file.write("  ")
                    version_file.write(value[0])
                    version_file.write(((40 - len(value[0]))* " "))
                    version_file.write("=  ")
                    version_file.write('\n')   
                elif len(value) == 2:
                    version_file.write("  ")
                    version_file.write(value[0])
                    version_file.write(((40 - len(value[0]))* " "))
                    version_file.write("=  ")
                    version_file.write(value[1])
                    version_file.write('\n')       
                else:
                    version_file.write('\n')            
    version_file.close()
    return version_file

ver8_data_dict, ver20_data_dict = ver8_and_ver20_data(file1 = "config_ver8.txt",file2 = "config_ver20.txt")
ver20_data_dict = value_add_to_list(ver8_data_dict)
version_file = version_file_write(ver20_data_dict)                               
