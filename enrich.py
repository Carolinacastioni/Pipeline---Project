from clean import df_clean
import pandas as pd
import json
import requests
import os
from dotenv import load_dotenv
load_dotenv()

apiKey = os.getenv("booksKey")
print("WE HAVE APIKEY") if apiKey else print("NO APIKEY FOUND")

def getVolumeID(path,queryParams=dict()):
    url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{path}"
    res = requests.get(url, params=queryParams)
    return res.json()

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

def getBooks(volume_id,queryParams=dict(),apiKey=""):
    url = f"https://www.googleapis.com/books/v1/volumes/{volume_id}"
    headers = {"Authorization":f"token {apiKey}"} if apiKey else {}
    res = requests.get(url, params=queryParams, headers=headers)
    return res.json()

lst_sales = []
for x in lst_book_info:
    book = getBooks(x)
    if book['saleInfo']['saleability'] == "NOT_FOR_SALE":
        pass
    else:
        enrich_data = (book['volumeInfo']['title'], book['saleInfo']['saleability'], book['saleInfo']['listPrice'], book['saleInfo']['retailPrice'], book['saleInfo']['buyLink'])
        lst_sales.append(enrich_data)

print(lst_sales[0])