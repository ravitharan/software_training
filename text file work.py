import re

ver8_file = open("config_ver8.txt", "r")
ver20_file = open("config_ver20.txt","r")
ver20_file_template = open("config_ver20_template.txt","r")
ver_file = open("config_ver.txt","w")
 
def version8_file_data(ver8_file):
    
    ver8_lines = ver8_file.readlines()

    ver8_data_list = []
    for line in ver8_lines:
        if ":" in line:
            continue
        else:
            line = re.sub(" +","",line)
            line = line.split("=")
            if len(line) == 2:  
                line[1] = line[1].strip().replace('\n', '')
                ver8_data_list.append(line)
    ver8_file.close()

    uniq_ver8_data = {}
    for data in ver8_data_list:
        count = 0
        for data1 in ver8_data_list:
            if data[0] == data1[0]:
                count += 1
        if count == 1:
           uniq_ver8_data[data[0]] = data[1] 
    #print(uniq_data)
           
    return uniq_ver8_data
uniq_ver8_data = version8_file_data(ver8_file)


def version20_file_data(ver20_file):
    
    ver20_lines = ver20_file.readlines() 

    ver20_data_list = []
    for ver20_line in ver20_lines:
        if ":" in ver20_line:
            continue
        else:
            ver20_line = re.sub(" +","",ver20_line)
            ver20_line = ver20_line.strip().replace('\n', '')
            ver20_data_list.append(ver20_line)
    ver20_file.close()

    uniq_ver20_data = []
    for data in ver20_data_list:
        count = 0
        u_data = []
        for data1 in ver20_data_list:
            if data == data1:
                count += 1
        if count == 1:
            u_data.append(data)
            uniq_ver20_data.append(u_data)
    #print(uniq_ver20_data)
            
    return uniq_ver20_data

uniq_ver20_data = version20_file_data(ver20_file)

def value_add_to_list(uniq_ver20_data):
    uniq_ver20_data_value = []
    
    for data in uniq_ver20_data:
        for key in uniq_ver8_data:
            if data != None and key != None:
                if data[0] == key:
                    data.append(uniq_ver8_data[key])
                    uniq_ver20_data_value.append(data)
    #print(uniq_ver20_data_value)
                    
    return uniq_ver20_data_value

uniq_ver20_data_value = value_add_to_list(uniq_ver20_data)
 
def version_file_data(ver_file):
    ver20_file = open("config_ver20.txt","r")
    ver20_lines = ver20_file.readlines()
    template_lines = ver20_file_template.readlines()
    for ver_line, temp_line in zip(ver20_lines,template_lines):
        ver_line = re.sub(" +","",ver_line)
        ver_line = ver_line.strip().replace('\n', '')
        temp_line = temp_line.strip().replace('\n', '')
        cu = 0
        for uniq_data in uniq_ver20_data_value:
            if uniq_data[0] == ver_line:
                cu += 1
                ver_file.write("  ")
                ver_file.write(temp_line)
                ver_file.write("   ")
                ver_file.write(uniq_data[1])
                ver_file.write('\n')
                continue
        else:
            if ":" in ver_line:
                ver_file.write(temp_line)
                ver_file.write('\n')
            elif len(ver_line) == 0:
                ver_file.write('\n')
            elif cu == 0:
                ver_file.write("  ")
                ver_file.write(temp_line)
                ver_file.write('\n')
         
    ver20_file.close()
    ver_file.close()
    
    return ver20_lines

ver20_lines = version_file_data(ver_file)




    
