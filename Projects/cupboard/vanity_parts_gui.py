import PySimpleGUI as sg
import os
from parse_vanity_info import *
from parse_order import *
from write_order_parts import *
from counter_top import *

if __name__ == '__main__':

    sg.set_options(font = 'Courier 20')

    sg.theme('DarkBlue16')
    layout = [
        [sg.Text('Select vanity order excel File: ', size=(35,2)),
            sg.InputText(), sg.FileBrowse(file_types = (("excel file", "*.xlsx"),))],
        [sg.Button('Ok'), sg.Button('Cancel')]
    ]

    # Create the Window
    window = sg.Window('Vanity parts order v2.0', layout)

    # Event Loop to process "events" and get the "values" of the inputs
    return_value = "cancel"
    while True:
        event, values = window.read()
        if event == 'Ok':
            input_xlsx = values[0]
            dst_path = os.path.dirname(input_xlsx)
            dst_path = os.path.join(dst_path, "output.xlsx")

            wb_in = openpyxl.load_workbook(input_xlsx)
            cupboard_parts = get_cupboard_list(wb_in)
            items = get_order_list(wb_in, cupboard_parts)

            wb_out = openpyxl.Workbook()
            ws = wb_out.active
            ws.title = SHEET_STYLE_COUNT
            wb_out.create_sheet(SHEET_COLOR_COUNT)
            wb_out.create_sheet(SHEET_STYLE_COLOR_COUNT)

            ws_vanity = [ wb_out[SHEET_STYLE_COUNT], wb_out[SHEET_COLOR_COUNT], wb_out[SHEET_STYLE_COLOR_COUNT] ]

            write_parts_for_workshop(ws_vanity, items)
            adjust_column_width(ws_vanity)

            # counter top
            counter_tops, sizes, colors, counts = get_counter_tops(wb_in)
            details =  get_countertop_details(counter_tops, sizes, colors)
            wb_out.create_sheet(SHEET_COUNTER_TOP)
            ws_ct = wb_out[SHEET_COUNTER_TOP]
            write_counter_top(ws_ct, 2, details, sizes, colors, counts)


            wb_out.save(dst_path)
            return_value = "pass"
            break
        elif event == 'Cancel' or event == sg.WIN_CLOSED: # if user closes window or clicks cancel
            break

    window.close()

    if return_value == "pass":
        sg.popup(f'\n  Output saved into {dst_path}!  \n', title="output file")
