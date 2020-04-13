from acquisition import *
from enrich import data_enrich
from clean import df_clean
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

#Enrich
volume_id = getVolumeID("9781612626864")
volume_id = volume_id['items'][0]['id']

apiKey = os.getenv("booksKey")
print("WE HAVE APIKEY") if apiKey else print("NO APIKEY FOUND")

book = getBooks(volume_id)

data_enrich = dataEnrich(book)

#Analysis
df_analisis = analisis(df_clean)

df_results = results(df_analisis)

#Result
title = input("Please write the book's title: ")
out_put = df_results[df_results.isin({title})]

print(out_put)