import openpyxl # THIS MODULE TO HANDLE xl FILES
from openpyxl.utils import get_column_letter
import sys

def xl_filter(user_xl_file, template):
    active_sheet = user_xl_file["Main Sheet"]
    template_sheet = template["Main Sheet"]
    maximum_row = active_sheet.max_row
    maximum_column = active_sheet.max_column

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

    for row in range(1, maximum_row + 1):
        """Header write"""
        if isinstance(active_sheet.cell(row, 1).value, str):
            if  "DATE ISSUE:" in active_sheet.cell(row, 1).value:
                column_num = [3, 8, 12, 13, 15, 21, 24, 33, 40]
                for column in column_num:
                    if column != 40:
                        template_sheet.cell(row, column).value = active_sheet.cell(row, column).value
                    else:
                        template_sheet.cell(row+1, column).value = active_sheet.cell(row+1, column).value
        """Write counter top existing row"""
        if active_sheet.cell(row, 30).value != None and isinstance(active_sheet.cell(row, 5).value, int):
            row_memory = row_num[0]
            for row_read in range(row , row+3):
                for column in range(1, maximum_column+1):
                    if active_sheet.cell(row_read, column).value != None:
                        template_sheet.cell(row_memory, column).value = active_sheet.cell(row_read, column).value
                row_memory += 1

            del row_num[0]
    template.save("ct_template.xlsx")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f'Argument error\nUsage: {sys.argv[0]} <user_excel_file> <template>')
        exit(1)
    user_xl_file = openpyxl.load_workbook(filename= sys.argv[1], data_only=True)
    template = openpyxl.load_workbook(filename=sys.argv[2])
    xl_filter(user_xl_file, template)
