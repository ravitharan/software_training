from openpyxl import load_workbook, Workbook, drawing
from PIL import Image
from openpyxl_image_loader import SheetImageLoader
from openpyxl.styles import *
from openpyxl.utils import *

wb_r = load_workbook("WORK.xlsx", data_only=True)
ws_r = wb_r["Main Sheet"]

wb_w = load_workbook("template.xlsx")
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
        ]
label_cell_map2 = [
        ('Q1', 'C6'),
        ('Q2', 'B8'),
        ('Q3', 'D6'),
        ('P4', 'H1'),
        ('J7', 'A6'),
        ]
label_cell_map3 = [
        ('Z1', 'C6'),
        ('Z2', 'B8'),
        ('Z3', 'D6'),
        ('Y4', 'H1'),
        ('S7', 'A6'),
        ]
column_count = 0
cu = 0
def add_row(cell_name, row_offset):
    (col, row) = cell.coordinate_from_string(cell_name)
    return col + str(row + row_offset)

for row_order in range(1, ws_r.max_row+1):
    cupboard_id  = ws_r["E" + str(row_order)].value
    if isinstance(cupboard_id, int):
        if column_count % 3 == 0 or column_count == 0 :
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
                dst_cell = add_row(dst, row_label - 1)
                src_cell = add_row(src, row_order - 6)
                #print(f'dst {dst_cell}, src {src_cell}')
                ws_w[dst_cell].value = ws_r[src_cell].value
            column_count += 1
            cu += 1
        else:
            if cu == 1:
                img = drawing.image.Image('logo.png')
                img.height=130
                img.width=200
                img.anchor = 'J'+str(1+row_label)
                ws_w.add_image(img)
                
                for (dst, src) in label_cell_map2:
                    dst_cell = add_row(dst, row_label - 1)
                    src_cell = add_row(src, row_order - 6)
                    #print(f'dst {dst_cell}, src {src_cell}')
                    ws_w[dst_cell].value = ws_r[src_cell].value
                column_count += 1
                cu += 1
            else:
                img = drawing.image.Image('logo.png')
                img.height=130
                img.width=200
                img.anchor = 'S'+str(1+row_label)
                ws_w.add_image(img)
                
                for (dst, src) in label_cell_map3:
                    dst_cell = add_row(dst, row_label - 1)
                    src_cell = add_row(src, row_order - 6)
                    #print(f'dst {dst_cell}, src {src_cell}')
                    ws_w[dst_cell].value = ws_r[src_cell].value
                column_count += 1
                cu = 0
                

wb_w.save("big_label.xlsx")
