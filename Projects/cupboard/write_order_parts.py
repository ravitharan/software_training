from parse_vanity_info import *
from parse_order import *

def write_parts_for_workshop(work_sheets, items):
    '''
    Seperate all items by material 
    '''
    materials = [ x[1] for x in items ]
    materials = list(set(materials))
    materials.sort()

    start_row = 1
    for material in materials:
        items_for_material = [x for x in items if x[1] == material]
        start_row += write_material_items(work_sheets, start_row, items_for_material)


def write_material_items(work_sheets, start_row, items):
    '''
    Write material & style header and seperate items by part name
    '''

    row = start_row
    for ws in work_sheets:
        ws.cell(row, 1).value = "MATERIAL"
        ws.cell(row, 2).value = items[0][1]
    row += 1

    styles = [ x[2] for x in items ]
    styles = list(set(styles))
    styles.sort()

    for ws in work_sheets:
        ws.cell(row, 1).value = "ITEM"
        ws.cell(row, 2).value = "SIZE"

        for i, style in enumerate(styles):
            ws.cell(row, i+3).value = style
    row += 1

    part_names = [ x[5] for x in items ]
    part_names = list(set(part_names))
    part_names.sort()

    for part_name in part_names:
        part_items = [x for x in items if x[5] == part_name]
        row = write_part_names(work_sheets, row, part_items, styles)
        row += 1

    return row

def write_part_names(work_sheets, start_row, items, styles):
    sizes = [ x[4] for x in items ]
    sizes = list(set(sizes))
    sizes = sorted(sizes, key = lambda x: int(x.split()[0]))

    row = start_row
    for ws in work_sheets:
        ws.cell(row, 1).value = items[0][5]

    for size in sizes:
        for ws in work_sheets:
            ws.cell(row, 2).value = size
        for i, style in enumerate(styles):
            counts = [x[0] for x in items if x[2] == style and x[4] == size ]
            if counts:
                work_sheets[0].cell(row, i+3).value = sum(counts)
                colors = [f'{x[0]} : {x[3]}' for x in items if x[2] == style and x[4] == size ]
                work_sheets[1].cell(row, i+3).value = '\n'.join(colors)
        row += 1

    work_sheets[0].cell(row, 1).value = "Total"
    work_sheets[0].cell(row, 2).value = f'=SUM(C{row}:{chr(ord("B") + len(styles))}{row})'
    for i, style in enumerate(styles):
        work_sheets[0].cell(row, i+3).value = f'=SUM({chr(ord("C") + i)}{row - len(sizes)}:{chr(ord("C") + i)}{row - 1})'
    row += 1

    return row

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f'Argument error\nUsage: {sys.argv[0]} <cupboard_excel_file>')
        exit(1)

    excel_file = sys.argv[1]
    wb = openpyxl.load_workbook(excel_file)
    cupboard_parts = get_cupboard_list(wb)
    items = get_order_list(wb, cupboard_parts)

    wb.create_sheet("PARTS DETAILS")
    wb.create_sheet("PARTS COLOR")
    ws = [ wb["PARTS DETAILS"], wb["PARTS COLOR"] ]

    write_parts_for_workshop(ws, items)

    wb.save('output.xlsx')

