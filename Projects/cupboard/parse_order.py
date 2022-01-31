from parse_vanity_info import *


def get_order_list(wb, cupboard_parts):
    '''
    Parse main sheet and get the order list
    '''
    ws = wb["Main Sheet"]
    work_week = ws['H1'].value
    print(f'WORK_WEEK {work_week}')

    ordered_parts = []
    for row in range(1, ws.max_row+1):
        cupboard = ws.cell(row,5).value
        if ('w' in str(cupboard)) or ('W' in str(cupboard)):
            continue
            
        elif(isinstance(cupboard,int)):
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
    for item_name in items:
        if item_name[5] == "TOWER MOULDING" or  item_name[5] == "DOOR MOULDING":
            item_name[5] = "MOULDING"
            
    # get framed mirror data into a list
    framed_mirror_data = []
    final_list = []
    for row in range(1, ws.max_row+1):
        cupboard = ws.cell(row,5).value
        if(isinstance(cupboard,int)):
            if ws.cell(row,13).value != None:
                framed_mirror_count = re.findall('\d+',ws.cell(row+2,13).value.strip())
                material = ws.cell(row,8).value.strip()
                style = ws.cell(row,7).value.strip()
                color = ws.cell(row,9).value.strip()
                size = ws.cell(row,13).value.strip()
                size = re.sub(' +', '',size)
                size =  size.replace("X" , " X ")
                size =  size.replace("W" , " W")
                size =  size.replace("H" , " H")
                framed_mirror_list = [int(framed_mirror_count[0]),f'{material}_{style}_{color}_{size}']
                framed_mirror_data.append(framed_mirror_list)
                 
    fr_set = set()
    for List in framed_mirror_data:
        fr_set.add(List[1])
    
    for data in fr_set:
        total = 0
        for List in framed_mirror_data:
            if data == List[1]:
                total += List[0]
         
        data = data.split('_')
        data.insert(0, total)
        data.insert(5, "FRAMED MIRROR")
        items.append(data)
    return (items, work_week)
            

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f'Argument error\nUsage: {sys.argv[0]} <cupboard_excel_file>')
        exit(1)

    excel_file = sys.argv[1]
    wb = openpyxl.load_workbook(excel_file, data_only=True)
    cupboard_parts = get_cupboard_list(wb)
    items, work_week = get_order_list(wb, cupboard_parts)

    #for p in items:
        #print(p)

