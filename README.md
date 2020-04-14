![](libros.jpg)

# Project | Pipelines Project

## Introduction

In this project we will clean the dataset "Book's dataset", that contains information about e-books, then we will enrich this dataset with Sales information from the Google books API documentation. Finally, we will create a data pipeline to process this data and produces the following result: The relation between List price and Retail price of a book and if this is a good deal. The project is compose by the following phases:

## Acquisition.py

Here we will import the CSV file of "Book's dataset". 

## Clean.py

We have cleaned the file by removing columns we won't use and deleting rows that doesn't have ISBN, which is a unique ID for each book and a crucial information in our analysis.


## Enrich.py

In this phase, we have imported sales information from the Google book API. Fist, we match the ISBN number to get the volume ID, an identifier ID on Google book API, then we used the volume ID to get the data that we need in our analysis. This API required authentication via token.

## Analysis.py

Now, we have created a dataframe with the sales information provided on the Enrich phase. The dataframe has the following information:

- Title
- Avability: If the book is for sale or not.
- Link: The link to buy the book in google play.
- List price: The suggested price for the book in EUR.
- Retail price: The actual price that books is saling in EUR.

## Results.py

We have merged both dataframes by the book's title and converted into one dataframe. Finally, we have compare the difference between the List price and the Retail and added this information on the dataframe. We created a final column with results, in which if the Retail price is higher than the List price this is a good deal, and when the list price is higher than the Retail price it's not an ideal deal.

## Main.py

We added all the pipeline mentioned above into this one phase, where the person just need to enter with the Book's title argument in order to get the result if this is a good deal or not and all the additional information of the book, such as the link to buy. 

