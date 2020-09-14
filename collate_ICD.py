import pandas as pd
import numpy as np

f = open("./original_data/txt/ICD.txt", "r")
data = {}
data['ICD-9-CM代碼'] = []
data['ICD-9-CM代碼英文名稱'] = []
data['ICD-9-CM代碼中文名稱'] = []
data['ICD-10-CM代碼'] = []
data['ICD-10-CM代碼英文名稱'] = []
data['ICD-10-CM代碼中文名稱'] = []
data['對應情形'] = []
exceptions = []
lines = f.readlines()
for line in lines:
    start = 0
    cur = 1
    while line[cur].isalpha() == False:
        cur += 1
    data['ICD-9-CM代碼'].append(line[start:cur].strip())
    start = cur
    while line[cur].isascii() == True or line[cur] == "’" or line[cur] == "Ⅰ" or line[cur] == "Ⅱ" or line[cur] == "Ⅲ":
        cur += 1
    while line[cur] != ' ':
        cur -= 1
    data['ICD-9-CM代碼英文名稱'].append(line[start:cur].strip())
    start = cur
    cur += 1
    while line[cur] != ' ':
        cur += 1
    data['ICD-9-CM代碼中文名稱'].append(line[start:cur].strip())
    start = cur
    if 'NoDx' in line:
        data['ICD-10-CM代碼'].append('')
        data['ICD-10-CM代碼英文名稱'].append('')
        data['ICD-10-CM代碼中文名稱'].append('')
        data['對應情形'].append(line[-6:].strip())
        continue
    cur += 1
    while line[cur] != ' ':
        cur += 1
    tmp = line[start:cur].strip()
    flag = 0
    for ch in tmp:
        if ch.isdigit():
            flag = 1
        if (ch.isalpha() == False and ch.isdigit() == False and ch != '.'):
            flag = 2
            cur -= 1
            while line[cur] != ' ':
                cur -= 1
            start -= 1
            while (line[start].isalpha() == True or line[start].isdigit() == True or line[start] == '.') and line[start].isascii():
                start -= 1
            start += 1
            tmp = line[start:cur].strip()
            data['ICD-9-CM代碼中文名稱'][len(data['ICD-9-CM代碼中文名稱'])-1] = data['ICD-9-CM代碼中文名稱'][len(data['ICD-9-CM代碼中文名稱'])-1][:-len(tmp)]
            break
    if flag == 0:
        cur -= 1
        while line[cur] != ' ':
            cur -= 1
        start -= 1
        while (line[start].isalpha() == True or line[start].isdigit() == True or line[start] == '.') and line[start].isascii():
            start -= 1
        start += 1
        tmp = line[start:cur].strip()
        data['ICD-9-CM代碼中文名稱'][len(data['ICD-9-CM代碼中文名稱'])-1] = data['ICD-9-CM代碼中文名稱'][len(data['ICD-9-CM代碼中文名稱'])-1][:-len(tmp)]
    data['ICD-10-CM代碼'].append(tmp)
    start = cur
    while line[cur].isascii() == True or line[cur] == "’" or line[cur] == "Ⅰ" or line[cur] == "Ⅱ" or line[cur] == "Ⅲ":
        cur += 1
    while line[cur] != ' ':
        cur -= 1
    data['ICD-10-CM代碼英文名稱'].append(line[start:cur].strip())
    start = cur
    data['ICD-10-CM代碼中文名稱'].append(line[start:-6].strip())
    data['對應情形'].append(line[-6:].strip())

df = pd.DataFrame(data)
df.to_csv('ICD.csv', index=False)
f.close()
