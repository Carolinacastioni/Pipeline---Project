from acquisition import df
import pandas as pd
import os

def drop_columns(*colunas):
    for c in colunas:
        return df.drop(columns=c)

def clean(df_clean):
    df_clean = drop_columns(['Unnamed: 0', 'rating', 'voters', 'price','currency', 'description', 'publisher', 'page_count', 'generes','language', 'published_date'])
    df_clean["check_duplicated"] = df_clean["ISBN"].duplicated()
    df_clean = df_clean.drop(df_clean[df_clean['check_duplicated'] == True].index)
    df_clean = df_clean.drop(columns=['check_duplicated'])
    df_clean = df_clean.set_index('ISBN')
    return df_clean

df_clean = clean(df)

df_clean = df_clean.drop('Original pages')
df_clean = df_clean.drop('Flowing text')
df_clean = df_clean.drop('Flowing text, Google-generated PDF')

