import PySimpleGUI as sg
import os
from parse_vanity_info import *
from parse_order import *
from write_order_parts import *

if __name__ == '__main__':

    sg.set_options(font = 'Courier 20')

    sg.theme('DarkBlue16')
    layout = [
        [sg.Text('Select vanity order excel File: ', size=(35,2)),
            sg.InputText(), sg.FileBrowse(file_types = (("excel file", "*.xlsx"),))],
        [sg.Button('Ok'), sg.Button('Cancel')]
    ]

    # Create the Window
    window = sg.Window('Vanity parts order v1.0', layout)

    # Event Loop to process "events" and get the "values" of the inputs
    return_value = "cancel"
    while True:
        event, values = window.read()
        if event == 'Ok':
            input_xlsx = values[0]
            dst_path = os.path.dirname(input_xlsx)
            dst_path = os.path.join(dst_path, "output.xlsx")

            wb = openpyxl.load_workbook(input_xlsx)
            cupboard_parts = get_cupboard_list(wb)
            items = get_order_list(wb, cupboard_parts)

            wb = openpyxl.Workbook()
            ws = wb.active
            ws.title = "PARTS DETAILS"
            wb.create_sheet("PARTS COLOR")
            ws = [ wb["PARTS DETAILS"], wb["PARTS COLOR"] ]

            write_parts_for_workshop(ws, items)

            wb.save(dst_path)
            return_value = "pass"
            break
        elif event == 'Cancel' or event == sg.WIN_CLOSED: # if user closes window or clicks cancel
            break

    window.close()

    if return_value == "pass":
        sg.popup(f'\n  Output saved into {dst_path}!  \n', title="output file")
