#!python
# -*- coding: UTF-8 -*-

import datetime
import random
import sys
import os
import openpyxl
import math
import statistics
import numpy as np

xls_template = './res/template.xlsx'

#===================================================通用
#pre0 生成随机数
def gen_random_range(left,right,round_cnt=None):
    if round_cnt:
        return round(random.uniform(left, right),round_cnt)
    else:
        return random.uniform(left, right)

#pre1 公式生存随机数(偏差小)

#pre2 把合格随机数写入xlsx
def open_xls(file_name):
    global wb
    global ws
    wb = openpyxl.load_workbook(xls_template, data_only=False)
    ws = wb[wb.sheetnames[0]]

def write_xls(row,col,data):
    ws.cell(row, col, data)
    wb.save(xls_template)

def read_xls(row, col):
    return ws.cell(row, col).value

#pre3 公式
def test_formula():
    print(round(1.23123,3))
    print(math.log(10,2))
    print(statistics.stdev([1,2,3]))
    print(np.mean([1,2,3]))
    print(np.std([1,2,3]))
    print(np.var([1,2,3]))

# ===================================================具体项
#0.主曲线+双对数

#1. 定标

#2. 准确度

#3. 最低检测限


#4. 线性


#5. 批内及批间精密度


#6. 特异性

#7. 批间差

#8. 校准品
#8.1 校准品均一性
#8.1.1 同批号五瓶校

#8.1.2 同一瓶五次测定

#8.2 校准品准确性


def auto_run():
    open_xls(xls_template)
    print(math.log(10,2))
    print(read_xls(1,1))

# test_formula()
# auto_run()
