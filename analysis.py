from enrich import data_enrich
from clean import df_clean
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()

def analisis(df):
    lst = [e for e in data_enrich]
    lst2 = [lp for lp in lst[2].values()]
    lst3 = [rp for rp in lst[3].values()]
    df["Availability"] = lst[1]
    df["List_Price(EUR)"] = float(lst2[0])
    df["Retail_Price(EUR)"] = float(lst3[0])
    df["Link"] = lst[4]
    return df

df_analisis = analisis(df_clean)

def results(df_results):
    df_results["Difference between List and Retail price"] = df_results["List_Price(EUR)"] - df_results["Retail_Price(EUR)"]
    df_results["Results_Description"] = df_results["Difference between List and Retail price"] > 0
    df_results.loc[df_results["Results_Description"] == True,"Results_Description"] = "Good deal! The retail prices is lower than the list price."
    df_results.loc[df_results["Results_Description"] == False,"Results_Description"] = "This is not ideal! The retail prices is higher than the list price."
    return df_results

df_results = results(df_analisis)

df_results = df_results.iloc[0]

a = df_results['Results_Description']
b = df_results['Difference between List and Retail price']
print(a, "The difference between the List Price and the Retail Price is",b,"€")