from openpyxl import load_workbook, Workbook, drawing
from PIL import Image
from openpyxl_image_loader import SheetImageLoader
from openpyxl.styles import *
from openpyxl.utils import *
import re
import sys

def get_vanity_info_data(wb):
    """
    Get cupboard  ID and Parts from column A and B in "VANITY INFO" sheet.Return dictionary of entries

    """
    wb_sheet = wb["VANITY INFO"]
    maximum_row = wb_sheet.max_row
    cupboard_id_parts = {}
    for x in range(1 , maximum_row + 1):
        value_A = wb_sheet["A" + str(x)].value
        value_B = wb_sheet["B" + str(x)].value
        if (type(value_A) == int) and (value_A != None) :
            value_B = re.sub(" +"," ", value_B)
            cupboard_id_parts[value_A] = value_B

    return cupboard_id_parts

def add_row(cell_name, row_offset):
    (col, row) = cell.coordinate_from_string(cell_name)
    return col + str(row + row_offset)

def cupboard_data_write(wb_r):
    """
    Main sheet and vanity info data write in to tha Label tamplate
    
    """
    ws_r = wb_r["Main Sheet"]
    ws_w = wb_w.active
    label_count = 0
    # row_label is as 1, 18, 33, 50, 65, 82, 97, 114, 129, 146, 161, 178, 193, 210
    row_label = 0
    label_cell_map = [
            ('H1', 'C6'),
            ('H2', 'B8'),
            ('H3', 'D6'),
            ('G4', 'H1'),
            ('A7', 'A6'),
            ('B9', 'F6'),
            ('B10','Dic'),
            ('F9', 'H6'),
            ('F10','G6'),
            ('F11','I6'),
            ('F12','L6'),
            ('G12','L7'),
            ('F13','K3'),
            ('B13','K6'),
            ('A13','K8')
            ]

    for row_order in range(1, ws_r.max_row+1):
        cupboard_id  = ws_r["E" + str(row_order)].value
        if isinstance(cupboard_id, int):
            label_count += 1
            if (label_count == 1):
                row_label = 1
            elif ((label_count % 2) == 0):
                row_label += 17
            else:
                row_label += 15
                
            #image insertion
            img = drawing.image.Image('logo.png')
            img.height=130
            img.width=200
            img.anchor = 'A'+str(1+row_label)
            ws_w.add_image(img)

            for (dst, src) in label_cell_map:
                if dst == 'B10':
                    dst_cell = add_row(dst, row_label - 1)
                    src_cell = cupboard_id_parts[cupboard_id]
                    ws_w[dst_cell].value = src_cell
                elif dst == 'G4':
                    dst_cell = add_row(dst, row_label - 1)
                    src_cell = ws_r["H1"].value
                    ws_w[dst_cell].value = src_cell
                else:
                    dst_cell = add_row(dst, row_label - 1)
                    src_cell = add_row(src, row_order - 6)
                    #print(f'dst {dst_cell}, src {src_cell}')
                    ws_w[dst_cell].value = ws_r[src_cell].value
     
    return label_cell_map

def framed_mirror_data_write(wb_r):
    """
    Main sheet data write in to tha Label tamplate
    
    """
    ws_r = wb_r["Main Sheet"]
    ws_w = wb_w.active
    label_count = 0
    # row_label is as 1, 18, 33, 50, 65, 82, 97, 114, 129, 146, 161, 178, 193, 210
    row_label = 0
    framed_label_cell_map = [
                            ('Q1', 'C6'),
                            ('Q2', 'B8'),
                            ('Q3', 'D6'),
                            ('P4', 'H1'),
                            ('J7', 'A6'),
                            ('K9', 'M6'),
                            ('K10','M3'),
                            ('O9', 'H6'),
                            ('O10','G6'),
                            ('O11','I6'),
                    
                            ]

    for row_order in range(1, ws_r.max_row+1):
        cupboard_id  = ws_r["E" + str(row_order)].value
        framed_mirror  = ws_r["M" + str(row_order)].value
        if isinstance(cupboard_id, int) and framed_mirror != None:
            label_count += 1
            if (label_count == 1):
                row_label = 1
            elif ((label_count % 2) == 0):
                row_label += 17
            else:
                row_label += 15
                
            #image insertion
            img = drawing.image.Image('logo.png')
            img.height=130
            img.width=200
            img.anchor = 'J'+str(1+row_label)
            ws_w.add_image(img)

            for (dst, src) in framed_label_cell_map:
                if dst == 'K10':
                    dst_cell = add_row(dst, row_label - 1)
                    src_cell = ws_r["M3"].value
                    ws_w[dst_cell].value = src_cell
                elif dst == 'P4':
                    dst_cell = add_row(dst, row_label - 1)
                    src_cell = ws_r["H1"].value
                    ws_w[dst_cell].value = src_cell
                else:
                    dst_cell = add_row(dst, row_label - 1)
                    src_cell = add_row(src, row_order - 6)
                    #print(f'dst {dst_cell}, src {src_cell}')
                    ws_w[dst_cell].value = ws_r[src_cell].value
     
    return framed_label_cell_map

def valance_data_write(wb_r):
    """
    Main sheet data write in to tha Label tamplate
    
    """
    ws_r = wb_r["Main Sheet"]
    ws_w = wb_w.active
    label_count = 0
    # row_label is as 1, 18, 33, 50, 65, 82, 97, 114, 129, 146, 161, 178, 193, 210
    row_label = 0
    valance_label_cell_map = [
                            ('Z1', 'C6'),
                            ('Z2', 'B8'),
                            ('Z3', 'D6'),
                            ('Y4', 'H1'),
                            ('S7', 'A6'),
                            ('T9', 'J6'),
                            ('T10','J3'),
                            ('X9', 'H6'),
                            ('X10','G6'),
                            ('X11','I6'),
                    
                            ]

    for row_order in range(1, ws_r.max_row+1):
        cupboard_id  = ws_r["E" + str(row_order)].value
        framed_mirror  = ws_r["J" + str(row_order)].value
        if isinstance(cupboard_id, int) and framed_mirror != None:
            label_count += 1
            if (label_count == 1):
                row_label = 1
            elif ((label_count % 2) == 0):
                row_label += 17
            else:
                row_label += 15
                
            #image insertion
            img = drawing.image.Image('logo.png')
            img.height=130
            img.width=200
            img.anchor = 'S'+str(1+row_label)
            ws_w.add_image(img)

            for (dst, src) in valance_label_cell_map:
                if dst == 'T10':
                    dst_cell = add_row(dst, row_label - 1)
                    src_cell = ws_r["J3"].value
                    ws_w[dst_cell].value = src_cell
                elif dst == 'Y4':
                    dst_cell = add_row(dst, row_label - 1)
                    src_cell = ws_r["H1"].value
                    ws_w[dst_cell].value = src_cell
                else:
                    dst_cell = add_row(dst, row_label - 1)
                    src_cell = add_row(src, row_order - 6)
                    #print(f'dst {dst_cell}, src {src_cell}')
                    ws_w[dst_cell].value = ws_r[src_cell].value
     
    return valance_label_cell_map

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(f'Argument error\nUsage: {sys.argv[0]} <wb> <wb_r> <wb_w>')
        exit(1)
    wb = load_workbook(filename= sys.argv[1], data_only=True)
    wb_r = load_workbook(filename= sys.argv[2], data_only=True)
    wb_w = load_workbook(filename= sys.argv[3])
     
    cupboard_id_parts = get_vanity_info_data(wb)
    label_cell_map = cupboard_data_write(wb_r)
    framed_label_cell_map = framed_mirror_data_write(wb_r)
    valance_label_cell_map = valance_data_write(wb_r)
    
    wb_w.save("big_label.xlsx")
