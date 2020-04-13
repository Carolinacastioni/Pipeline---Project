from acquisition import *
from clean import *
from enrich import *
from analysis import *
from results import *
import pandas as pd
import os
import json
import requests
from bs4 import BeautifulSoup
from argparse import ArgumentParser

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
result = results(df_analisis)

#Call
def parse():
    parser=ArgumentParser(description="This program returns the analysis between list price and retail price of a book")
    parser.add_argument("--title",dest="title",type=str, help="Write the whole book title.")
    parser.add_argument("--budget",dest="budget",type=int,help="Write the max. price you will pay for the book.")
    return parser.parse_args()

def main():
    args = parse()
    title=args.title
    budget=args.budget
    try:
        print(books_analysis(title,budget))
    except Exception:
        print("You must introduce a valid title and budget")

if __name__ == "__main__":
    main()

