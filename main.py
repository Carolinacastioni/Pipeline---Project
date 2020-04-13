from acquisition import *
from clean import *
from enrich import *
from analysis import *
from results import *
import pandas as pd
import os
import json
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
load_dotenv()

#Acquisition
df = open_file("/home/carolina/Desktop/IRONHACK/Project files/books.csv")

#Clean
df_clean = clean(df)

df_clean = df_clean.drop('Original pages')
df_clean = df_clean.drop('Flowing text')
df_clean = df_clean.drop('Flowing text, Google-generated PDF')

#Enrich
apiKey = os.getenv("booksKey")
print("WE HAVE APIKEY") if apiKey else print("NO APIKEY FOUND")

lst_vid = []
for e in df_clean.index:
    v_id = getVolumeID(e)
    a = v_id.get('items',[{}])[0].get('id',"")
    lst_vid.append(a)

lst_book_info = []
for v in lst_vid:
    if v == "":
        pass
    else:
        lst_book_info.append(v)

lst_sales = []
for x in lst_book_info:
    book = getBooks(x)
    if book['saleInfo']['saleability'] == "NOT_FOR_SALE":
        pass
    else:
        enrich_data = (book['volumeInfo']['title'], book['saleInfo']['saleability'], book['saleInfo']['listPrice'], book['saleInfo']['retailPrice'], book['saleInfo']['buyLink'])
        lst_sales.append(enrich_data)

#Analysis
data = {}
data['title'] = [e[0] for e in lst_sales]
data['Avability'] = [e[1] for e in lst_sales]
data["Link"] = [l[4] for l in lst_sales]
data["List price (EUR)"] = [lp[2]['amount'] for lp in lst_sales]
data['Retail price (EUR)'] = [rp[3]['amount'] for rp in lst_sales]

df_sales_info = pd.DataFrame(data)

df_analisis = pd.merge(df_clean, df_sales_info, on='title')

df_analisis['List price (EUR)'] = df_analisis['List price (EUR)'].astype(float)
df_analisis['Retail price (EUR)'] = df_analisis['Retail price (EUR)'].astype(float)

#Result
results = results(df_analisis)

title = input("Please write the book's title: ")
dataframe_filtrado = results[results['title'] == {title}]

print(dataframe_filtrado)