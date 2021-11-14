import openpyxl # THIS MODULE TO HANDLE xl FILES
from openpyxl.utils import get_column_letter
import sys

def xl_filter(user_xl_file, template):
    active_sheet = user_xl_file["Main Sheet"]
    template_sheet = template["Sheet1"]
    maximum_row = active_sheet.max_row
    maximum_column = active_sheet.max_column
    """Head write"""
    template_sheet["C1"] = active_sheet["C1"].value
    template_sheet["C30"] = active_sheet["C30"].value
    template_sheet["H1"] = active_sheet["H1"].value
    template_sheet["H30"] = active_sheet["H30"].value
    template_sheet["X1"] = active_sheet["X1"].value
    template_sheet["X30"] = active_sheet["X30"].value
    template_sheet["AC1"] = active_sheet["AC1"].value
    template_sheet["AC30"] = active_sheet["AC30"].value
    template_sheet["AG1"] = active_sheet["AG1"].value
    template_sheet["AG30"] = active_sheet["AG30"].value
    
    """Write counter top order details"""
    row_num = []
    i = 6
    add = 1
    while i < maximum_row:
        if add % 9 != 0:
            row_num.append(i)
            i += 3
        else:
            i += 5
        add += 1


    for row in range(6 , maximum_row+1):
        if active_sheet["AD" + str(row)].value != None:
            if "COMPANY" in active_sheet[get_column_letter(1) + str(row)].value:
                template_sheet[get_column_letter(1) + str(row_num[0])] = active_sheet[get_column_letter(1) + str(row)].value
                template_sheet[get_column_letter(1) + str(row_num[0]+2)] = active_sheet[get_column_letter(1) + str(row+2)].value
                template_sheet[get_column_letter(2) + str(row_num[0]+2)] = active_sheet[get_column_letter(2) + str(row+2)].value
                for col in range(3,10):
                    template_sheet[get_column_letter(col) + str(row_num[0])] = active_sheet[get_column_letter(col) + str(row)].value
                for col in range(10,12):
                    template_sheet[get_column_letter(col) + str(row_num[0])] = active_sheet[get_column_letter(col) + str(row)].value
                    template_sheet[get_column_letter(col) + str(row_num[0]+2)] = active_sheet[get_column_letter(col) + str(row+2)].value
                template_sheet[get_column_letter(12) + str(row_num[0])] = active_sheet[get_column_letter(12) + str(row)].value
                template_sheet[get_column_letter(12) + str(row_num[0]+1)] = active_sheet[get_column_letter(12) + str(row+1)].value
                template_sheet[get_column_letter(12) + str(row_num[0]+2)] = active_sheet[get_column_letter(12) + str(row+2)].value
                template_sheet[get_column_letter(13) + str(row_num[0])] = active_sheet[get_column_letter(13) + str(row)].value
                template_sheet[get_column_letter(13) + str(row_num[0]+2)] = active_sheet[get_column_letter(13) + str(row+2)].value
                for col in range(14,27):
                    template_sheet[get_column_letter(col) + str(row_num[0])] = active_sheet[get_column_letter(col) + str(row)].value
                template_sheet[get_column_letter(27) + str(row_num[0])] = active_sheet[get_column_letter(27) + str(row)].value
                template_sheet[get_column_letter(28) + str(row_num[0])] = active_sheet[get_column_letter(28) + str(row)].value
                template_sheet[get_column_letter(28) + str(row_num[0]+2)] = active_sheet[get_column_letter(28) + str(row+2)].value
                template_sheet[get_column_letter(29) + str(row_num[0]+2)] = active_sheet[get_column_letter(29) + str(row+2)].value
                for col in range(30,41):
                    template_sheet[get_column_letter(col) + str(row_num[0])] = active_sheet[get_column_letter(col) + str(row)].value
                del row_num[0]
    template.save("ct_template.xlsx")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f'Argument error\nUsage: {sys.argv[0]} <user_excel_file> <template>')
        exit(1)
    user_xl_file = openpyxl.load_workbook(filename= sys.argv[1], data_only=True)
    template = openpyxl.load_workbook(filename=sys.argv[2])
    xl_filter(user_xl_file, template)

    


    
       
        

    

