apiKey = os.getenv("booksKey")
print("WE HAVE APIKEY") if apiKey else print("NO APIKEY FOUND")

def getBooks(volume_id=volume_id,queryParams=dict(),apiKey=""):
    url = f"https://www.googleapis.com/books/v1/volumes/{volume_id}"
    headers = {"Authorization":f"token {apiKey}"} if apiKey else {}
    res = requests.get(url, params=queryParams, headers=headers)
    return res.json()

book = getBooks(volume_id)

def dataEnrich(book):
    if book['saleInfo']['saleability'] == "NOT_FOR_SALE":
        return "No available for sale"
    else:
        enrich_data = (book['volumeInfo']['title'], book['saleInfo']['saleability'], book['saleInfo']['listPrice'], book['saleInfo']['retailPrice'], book['saleInfo']['buyLink'])
        return enrich_data

data_enrich = dataEnrich(book)
print(data_enrich)