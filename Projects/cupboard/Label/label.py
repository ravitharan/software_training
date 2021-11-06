from openpyxl import load_workbook, Workbook, drawing
from PIL import Image
from openpyxl_image_loader import SheetImageLoader
from openpyxl.styles import *

wb_r = load_workbook("Cupboard.xlsx", data_only=True)
ws_r = wb_r["Main Sheet"]

wb_w = load_workbook("CupboardTemplate.xlsx")
ws_w = wb_w.active

#label count
n=0
#move row to next label
row_num = 0

for row in range(6, ws_r.max_row+1):
    if(ws_r["O"+str(row)].value) == 'Q':
        n += 1
        #image insertion
        """
        img = drawing.image.Image('logo.png')
        img.height=120
        img.width=200
        img.anchor = 'A'+str(1+row_num)
        ws_w.add_image(img)
        """
        #order details
        ws_w["H"+str(1+row_num)].value = ws_r["C"+str(row)].value
        ws_w["H"+str(2+row_num)].value = ws_r["B"+str(row+2)].value
        ws_w["H"+str(4+row_num)].value = ws_r["D"+str(row)].value
        ws_w["H"+str(5+row_num)].value = ws_r["H1"].value
        ws_w["A"+str(7+row_num)].value = ws_r["A"+str(row)].value
        
        #item info
        ws_w["B"+str(9+row_num)].value = ws_r["AF"+str(row)].value
        ws_w["A"+str(9+row_num)].value = 1
        if(ws_r["AF"+str(row)].value != None):
            ws_w["B"+str(10+row_num)].value = ws_r["Y3"].value
            ws_w["A"+str(10+row_num)].value = 1
        if(ws_r["Y"+str(row)].value != None and ws_r["Z"+str(row)].value != None):
            ws_w["B"+str(11+row_num)].value = ws_r["AM"+str(row)].value
            ws_w["C"+str(11+row_num)].value = ws_r["AM3"].value
            ws_w["A"+str(11+row_num)].value = 1       
        ws_w["B"+str(13+row_num)].value = ws_r["AA"+str(row)].value
        
        #item descriotion
        ws_w["F"+str(9+row_num)].value = ws_r["AG3"].value
        ws_w["G"+str(9+row_num)].value = ws_r["AG"+str(row)].value
        ws_w["F"+str(10+row_num)].value = ws_r["AH3"].value
        ws_w["G"+str(10+row_num)].value = ws_r["AH"+str(row)].value
        ws_w["F"+str(11+row_num)].value = ws_r["AI3"].value
        ws_w["G"+str(11+row_num)].value = ws_r["AI"+str(row)].value
        ws_w["F"+str(12+row_num)].value = ws_r["AK3"].value
        ws_w["G"+str(12+row_num)].value = ws_r["AK"+str(row)].value
        ws_w["F"+str(13+row_num)].value = ws_r["AJ3"].value
        ws_w["G"+str(13+row_num)].value = ws_r["AJ"+str(row)].value
        
        row_num +=15

wb_w.save("CupboardTemplate.xlsx")

print("count" , n)

