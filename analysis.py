from enrich import lst_sales
from clean import df_clean
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()

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

