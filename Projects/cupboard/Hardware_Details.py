import re
import sys
import openpyxl
from openpyxl.styles import *
from openpyxl.utils import get_column_letter

def hardware_data(excel_file):
    current_sheet = excel_file["Main Sheet"] # Active VANITY INFO sheet
    maximum_row = current_sheet.max_row
    hardware_count_items = []
    for x in range(1 , maximum_row + 1):
        cupboard_id = current_sheet["E" + str(x)].value
        if type(cupboard_id) == int and   x < 100:
            count_items = []
            c = x + 2
            hardware_count  = current_sheet["L" + str(c)].value
            if hardware_count != None:
                hardware_count = hardware_count.replace('[', '')
                hardware_count = hardware_count.replace(']', '')
                hardware_count = hardware_count.replace('+', '_')
                hardware_count = hardware_count.split('_')
                for count in hardware_count:
                    count_items.append(int(count))
                    
                hardware_item1 = current_sheet["L" + str(x)].value
                hardware_item2 = current_sheet["L" + str(x+1)].value
                if 'DR-' in hardware_item1:
                    hardware_item1 = hardware_item1.replace('DR-','')
                elif 'DW-' in hardware_item1:
                    hardware_item1 = hardware_item1.replace('DW-','')
                count_items.append(hardware_item1)
                
                if hardware_item2 != None:   
                    if 'DR-' in hardware_item2 :
                        hardware_item2 = hardware_item2.replace('DR-','')
                         
                    elif 'DW-' in hardware_item2:
                        hardware_item2 = hardware_item2.replace('DW-','')
                 
                if  hardware_item2!= None and hardware_item2 != hardware_item1 :
                    count_items.append(hardware_item2)
            
                hardware_count_items.append(count_items) 
                
    return hardware_count_items
 
def hardware_add_count(hardware_count_item):
    hardware_item_set = set()
    for item_list in hardware_count_item:
        if len(item_list) == 4:
            hardware_item_set.add(item_list[2])
            hardware_item_set.add(item_list[3])
        else:
            hardware_item_set.add(item_list[1])

    hardware_count_Dict = {}
    for set_item in hardware_item_set:
        total = 0
        for list_item in hardware_count_item:
            if len(list_item)== 4:
                if list_item[2] == set_item:
                    total += list_item[0]
                if list_item[3] == set_item:
                    total += list_item[1]
            else:
                if list_item[1] == set_item:
                    total += list_item[0]
                    
        hardware_count_Dict[set_item] = total
    
    return hardware_count_Dict

def Hardware_Details_Write(hardware_count_Dict_data):
    column_number1, column_number2 = 1, 2
    column = str(chr(64 + column_number1))
    sheet.column_dimensions[column].width = 24
    column = str(chr(64 + column_number2))
    sheet.column_dimensions[column].width = 24
    
    sheet['A1'] = 'Hardware Item' # Excel_cell
    sheet['A1'].font = Font(bold=True, size = 16)
    sheet['A1'].fill = PatternFill(fgColor="61E43A", fill_type = "solid")
    sheet['A1'].alignment = Alignment(horizontal='center')
    
    sheet['B1'] = 'Count' # Excel_cell
    sheet['B1'].font = Font(bold=True, size = 16)
    sheet['B1'].fill = PatternFill(fgColor="61E43A", fill_type = "solid")
    sheet['B1'].alignment = Alignment(horizontal='center')

    row = 2
    total = 0
    for key in hardware_count_Dict_data:
        sheet["A" + str(row)] = key # Excel_cell_value_add
        sheet["B" + str(row)] = hardware_count_Dict_data[key] # Excel_cell_value_add
        sheet["B"+ str(row)].alignment = Alignment(horizontal='center')
        total += sheet["B" + str(row)].value
        row += 1
    
    sheet["A" + str(row+1)] = "Total"
    sheet["A" + str(row+1)].font = Font(bold=True, size = 12)
    
    sheet["B" + str(row+1)] = total
    sheet["B" + str(row+1)].font = Font(bold=True, size = 12)
    sheet["B"+ str(row+1)].alignment = Alignment(horizontal='center')
    
    return row

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f'Argument error\nUsage: {sys.argv[0]} <cupboard_excel_file>')
        exit(1)

excel_file = sys.argv[1]    
excel_file = openpyxl.load_workbook(excel_file, data_only=True)
hardware_count_items = hardware_data(excel_file)
hardware_count_Dict = hardware_add_count(hardware_count_item)   

excel_file = openpyxl.Workbook()
sheet = workbook.active
sheet.title = Hardware_Details
Hardware_Details_Write(hardware_count_Dict_data)

workbook.save('Hardware Item Details.xlsx') # New Excel file create
