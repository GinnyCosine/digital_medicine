from os import rename
from os import listdir
import pandas as pd
import numpy as np

mypath = "./original_data/txt/OO/"
files = listdir(mypath)
data = {
        'FEE_YM'       :[],
        'APPL_TYPE'    :[],
        'HOSP_ID'      :[],
        'APPL_DATE'    :[],
        'CASE_TYPE'    :[],
        'SEQ_NO'       :[],
        'ORDER_TYPE':[],
        'DRUG_NO':[],
        'DRUG_USE':[],
        'DRUG_FRE':[],
        'UNIT_PRICE'    :[],
        'TOTAL_QTY'    :[],
        'TOTAL_AMT'  :[]
    }
for file_ in files:
    year = int(file_[2:6])
    if year <= 2006:
        data_type = 1
    elif year <= 2011:
        data_type = 2
    elif year >= 2012:
        data_type = 3
    
    f = open(mypath + file_, "r")
    lines = f.readlines()
    for line in lines:
        # 85~95
        data['FEE_YM'].append(line[:6].strip())
        data['APPL_TYPE'].append(line[6].strip())
        data['HOSP_ID'].append(line[7:41].strip())
        data['APPL_DATE'].append(line[41:49].strip())
        data['CASE_TYPE'].append(line[49:51].strip())
        data['SEQ_NO'].append(line[51:57].strip())
        data['ORDER_TYPE'].append(line[57].strip())
        data['DRUG_NO'].append(line[58:70].strip())
        data['DRUG_USE'].append(line[70:76].strip())
        data['DRUG_FRE'].append(line[76:94].strip())
        data['UNIT_PRICE'].append(line[94:104].strip())
        data['TOTAL_QTY'].append(line[104:111].strip())
        data['TOTAL_AMT'].append(line[111:119].strip())

    f.close()
df = pd.DataFrame(data)
df.to_csv('OOall.csv', index=False)