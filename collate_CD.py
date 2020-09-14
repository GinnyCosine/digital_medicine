from os import rename
from os import listdir
import pandas as pd
import numpy as np

df = pd.read_csv('./original_data/csv/ICD.csv')

icd9 = df['ICD-9-CM代碼']
icd10 = df['ICD-10-CM代碼']

dic = {}
for idx in range(0, len(icd10)):
    if icd9[idx][0].isdigit():
        sp = icd9[idx].split('.')
        tmp = ''
        for x in sp:
            tmp += x
        dic[icd10[idx]] = tmp
    else:
        dic[icd10[idx]] = icd9[idx]

mypath = "./original_data/txt/CD/"
files = listdir(mypath)
data = {
        'FEE_YM'       :[],
        'APPL_TYPE'    :[],
        'HOSP_ID'      :[],
        'APPL_DATE'    :[],
        'CASE_TYPE'    :[],
        'SEQ_NO'       :[],
        'CURE_ITEM_NO1':[],
        'CURE_ITEM_NO2':[],
        'CURE_ITEM_NO3':[],
        'CURE_ITEM_NO4':[],
        'FUNC_TYPE'    :[],
        'FUNC_DATE'    :[],
        'ID_BIRTHDAY'  :[],
        'ID'           :[],
        'ACODE_ICD9_1' :[],
        'ACODE_ICD9_2' :[],
        'ACODE_ICD9_3' :[],
        'ICD_OP_CODE'  :[],
        'DRUG_DAY'     :[],
        'MED_TYPE'     :[],
        'ID_SEX'       :[]
    }
for file_ in files:
    year = int(file_[2:6])
    if year <= 2003:
        data_type = 1
    elif year <= 2011:
        data_type = 2
    elif year >= 2012:
        data_type = 3
    
    f = open(mypath + file_, "r")
    lines = f.readlines()
    for line in lines:
        data['FEE_YM'].append(line[:6].strip())
        data['APPL_TYPE'].append(line[6].strip())
        data['HOSP_ID'].append(line[7:41].strip())
        data['APPL_DATE'].append(line[41:49].strip())
        data['CASE_TYPE'].append(line[49:51].strip())
        data['SEQ_NO'].append(line[51:57].strip())
        data['CURE_ITEM_NO1'].append(line[57:59].strip())
        data['CURE_ITEM_NO2'].append(line[59:61].strip())
        data['CURE_ITEM_NO3'].append(line[61:63].strip())
        data['CURE_ITEM_NO4'].append(line[63:65].strip())
        data['FUNC_TYPE'].append(line[65:67].strip())
        data['FUNC_DATE'].append(line[67:75].strip())
        data['ID_BIRTHDAY'].append(line[83:91].strip())
        data['ID'].append(line[91:123].strip())
        if data_type == 1:
            tmp1 = line[130:135].strip()
            tmp2 = line[135:140].strip()
            tmp3 = line[140:145].strip()
            t = dic.get(tmp1)
            if t != None:
                tmp1 = t
            t = dic.get(tmp2)
            if t != None:
                tmp2 = t
            t = dic.get(tmp3)
            if t != None:
                tmp3 = t
            if tmp1.isdigit():
                tmp1 = tmp1[0:3] + '.' + tmp1[3:]
            if tmp2.isdigit():
                tmp2 = tmp2[0:3] + '.' + tmp2[3:]
            if tmp3.isdigit():
                tmp3 = tmp3[0:3] + '.' + tmp3[3:]
            data['ACODE_ICD9_1'].append(tmp1)
            data['ACODE_ICD9_2'].append(tmp2)
            data['ACODE_ICD9_3'].append(tmp3)
            data['ICD_OP_CODE'].append(line[145:149].strip())
            data['DRUG_DAY'].append(line[149:151].strip())
            data['MED_TYPE'].append(line[151].strip())
            data['ID_SEX'].append(line[298].strip())
        elif data_type == 2:
            tmp1 = line[131:136].strip()
            tmp2 = line[136:141].strip()
            tmp3 = line[141:146].strip()
            t = dic.get(tmp1)
            if t != None:
                tmp1 = t
            t = dic.get(tmp2)
            if t != None:
                tmp2 = t
            t = dic.get(tmp3)
            if t != None:
                tmp3 = t
            if tmp1.isdigit():
                tmp1 = tmp1[0:3] + '.' + tmp1[3:]
            if tmp2.isdigit():
                tmp2 = tmp2[0:3] + '.' + tmp2[3:]
            if tmp3.isdigit():
                tmp3 = tmp3[0:3] + '.' + tmp3[3:]
            data['ACODE_ICD9_1'].append(tmp1)
            data['ACODE_ICD9_2'].append(tmp2)
            data['ACODE_ICD9_3'].append(tmp3)
            data['ICD_OP_CODE'].append(line[146:150].strip())
            data['DRUG_DAY'].append(line[150:152].strip())
            data['MED_TYPE'].append(line[152].strip())
            data['ID_SEX'].append(line[299].strip())
        elif data_type == 3:
            tmp1 = line[131:146].strip()
            tmp2 = line[146:161].strip()
            tmp3 = line[161:176].strip()
            t = dic.get(tmp1)
            if t != None:
                tmp1 = t
            t = dic.get(tmp2)
            if t != None:
                tmp2 = t
            t = dic.get(tmp3)
            if t != None:
                tmp3 = t
            if tmp1.isdigit():
                tmp1 = tmp1[0:3] + '.' + tmp1[3:]
            if tmp2.isdigit():
                tmp2 = tmp2[0:3] + '.' + tmp2[3:]
            if tmp3.isdigit():
                tmp3 = tmp3[0:3] + '.' + tmp3[3:]
            data['ACODE_ICD9_1'].append(tmp1)
            data['ACODE_ICD9_2'].append(tmp2)
            data['ACODE_ICD9_3'].append(tmp3)
            data['ICD_OP_CODE'].append(line[176:191].strip())
            data['DRUG_DAY'].append(line[191:193].strip())
            data['MED_TYPE'].append(line[193].strip())
            data['ID_SEX'].append(line[340].strip())
    f.close()
df = pd.DataFrame(data)
df.to_csv('CD1996_2013.csv', index=False)