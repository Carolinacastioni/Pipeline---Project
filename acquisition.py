import pandas as pd
import os

def open_file(file):
    df = pd.read_csv(file, error_bad_lines=False)
    return df

df = open_file("/home/carolina/Desktop/IRONHACK/Project files/books.csv")