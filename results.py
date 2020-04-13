from analysis import df_analisis
import pandas as pd

def results(df_results):
    df_results["Difference between List and Retail price"] = df_results["List price (EUR)"] - df_results["Retail price (EUR)"]
    df_results["Results_Description"] = df_results["Difference between List and Retail price"] >= 0
    df_results.loc[df_results["Results_Description"] == True,"Results_Description"] = "Good deal! The retail prices is lower than the list price."
    df_results.loc[df_results["Results_Description"] == False,"Results_Description"] = "This is not ideal! The retail prices is higher than the list price."
    return df_results

results = results(df_analisis)