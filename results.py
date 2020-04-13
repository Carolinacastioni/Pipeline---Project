from analysis import df_analisis
import pandas as pd

def results(df_results):
    df_results["Difference between List and Retail price"] = df_results["List price (EUR)"] - df_results["Retail price (EUR)"]
    df_results["Results_Description"] = df_results["Difference between List and Retail price"] >= 0
    df_results.loc[df_results["Results_Description"] == True,"Results_Description"] = "Good deal! The retail prices is lower than the list price."
    df_results.loc[df_results["Results_Description"] == False,"Results_Description"] = "This is not ideal! The retail prices is higher than the list price."
    return df_results

result = results(df_analisis)

def books_analysis(title, budget):
    new_df = result[result['title'] == str(title)]
    new_dff = new_df[new_df['Retail price (EUR)'] <= int(budget)]
    if new_dff.empty == True:
        return "Sorry, we don't have any book available with this title in this budget"
    else:
        return new_dff

