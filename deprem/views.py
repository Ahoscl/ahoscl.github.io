from django.shortcuts import render
from .models import Deprem
import pandas as pd
import sqlite3
# Create your views here.


def index(request):
    con=sqlite3.connect(database='db.sqlite3')
    cur=con.cursor()
    df2=pd.read_sql('select * from deprem_deprem',con,parse_dates=True)
    #df2.columns.names=['a','b','c','d','e','f','g']


    veri=Deprem.objects.all()
    tablo=pd.DataFrame(veri)

    tablo.to_html()
    context={'bilgi':tablo.to_html(),
             'sql':df2.to_html()}
    return render(request,'depremindex.html',context)