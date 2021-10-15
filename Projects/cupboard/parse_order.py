from parse_vanity_info import *

def get_order_list(wb, cupboard_parts):
    '''
    Parse main sheet and get the order list
    '''
    ws = wb["Main Sheet"]

    ordered_parts = []
    for row in range(1, ws.max_row+1):
        cupboard = ws.cell(row,5).value
        if(isinstance(cupboard,int)):
            material = ws.cell(row,8).value.strip()
            style = ws.cell(row,7).value.strip()
            color = ws.cell(row,9).value.strip()
            parts = cupboard_parts[cupboard]
            parts_details = [ [x[0], f'{material}_{style}_{color}_{x[1]}_{x[2]}'] for x in parts ]
            for new in parts_details:
                for i, exist in enumerate(ordered_parts):
                    if (new[1] == exist[1]):
                        ordered_parts[i][0] += new[0] # Add the count for same parts
                        break
                else:
                    ordered_parts.append(new)
    order = []
    for x in ordered_parts:
        details = x[1].split('_')
        details.insert(0, x[0])
        order.append(details)

    #Sort by material, name, size, style and color
    items = sorted(order, key=lambda item: (item[1], item[5], item[4], item[2], item[3]))

    return items
            

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f'Argument error\nUsage: {sys.argv[0]} <cupboard_excel_file>')
        exit(1)

    excel_file = sys.argv[1]
    wb = openpyxl.load_workbook(excel_file)
    cupboard_parts = get_cupboard_list(wb)
    items = get_order_list(wb, cupboard_parts)

    for p in items:
        print(p)

