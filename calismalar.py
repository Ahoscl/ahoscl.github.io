import sqlite3
import matplotlib.pyplot as plt
import pandas as pd

connection=sqlite3.connect('db.sqlite3')
#id    enlem   boylam  derinlik  buyukluk yer

#todo verileri düzgünce çek
veri=pd.read_sql('select * from deprem_deprem',connection,index_col='olus_zamani',parse_dates=True)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

#print(veri[veri.index=='2003.01.31 16:59:49'])



"""
for deneme in veri.yer:
    if '(' in deneme:
        a=[i.split('(') for i in veri.yer]
        print(a)

    else:
        print(deneme)

"""


""" 
for i,j in list(i.split('(') for i in veri.yer):
    print(i,j.replace(')',''))

"""

