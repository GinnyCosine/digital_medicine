from os import rename
from os import listdir

mypath = "./OO/"
files = listdir(mypath)
for f in files:
    tmp = f.split('.')[0]
    name = tmp.split('_')[1]
    rename(mypath + f, mypath + name +'.txt')