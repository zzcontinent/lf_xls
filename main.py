import datetime
import sys
import os
import openpyxl
import wps
import pywps

xls_st2 = '/home/cliff/tmp/st2.xlsx'

wb_r = openpyxl.load_workbook(xls_st2, data_only=True)
wb_w = openpyxl.load_workbook(xls_st2, data_only=False)
ws_r = wb_r.get_sheet_by_name(wb_r.get_sheet_names()[0])
ws_w = wb_w.get_sheet_by_name(wb_w.get_sheet_names()[0])

def input_acuracy_3(input_3):
    origin_input_3=[]
    origin_input_3.append(ws_r.cell(34,3).value)
    origin_input_3.append(ws_r.cell(35,3).value)
    origin_input_3.append(ws_r.cell(36,3).value)
    print(origin_input_3)
    ws_w.cell(34,3,input_3[0])
    ws_w.cell(35,3,input_3[1])
    ws_w.cell(36,3,input_3[2])
    wb_w.save(xls_st2)
    pywps.inout.inputs
    print(ws_r.cell(40,3).value)
    print(ws_r.cell(40,2).value)

input_acuracy_3([0.5,0.52,0.53])
