

import csv
import requests
from bs4 import BeautifulSoup


products=[]              #List to store the name of the product
prices=[]                #List to store price of the product
ratings=[]               #List to store rating of the product

for i in range(2,12):
    url ="https://www.flipkart.com/search?q=tv&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_8_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_8_0_na_na_na&as-pos=8&as-type=TRENDING&suggestionId=tv&requestId=9c9fa553-b7e5-454b-a65b-bbb7a9c74a29"+str(i)
    page = requests.get(url)
    #print(page.content)

    r = requests.get(url)

    soup = BeautifulSoup(r.text,"lxml")
    #while True :
    #np = soup.find("a",class_ = "_1LKT03").get("href")
    #cnp = "https://www.flipkart.com/"+np
    soup = BeautifulSoup(page.content, 'html.parser')
    # box = soup.find("div",class_="_1YokD2 _3Mn1Gg")
    box = soup.find("div", class_="_1YokD2 _3Mn1Gg")
if box is not None:
    names = box.find_all("div", class_="_4rR01T")
    # ... and similarly for ratings and prices
else:
    print("Box variable is None. Cannot find names, ratings, or prices.")
    #it gives us the visual representation of data
    names=box.find_all("div",class_="_4rR01T")
    

    for i in names :
        name = i.text
        products.append(names)
    print(products)
    #get rating of a product
    
    rating=box.find_all("div",class_="_3LWZlK")
    for i in ratings:
        name = i.text
        ratings.append(name)
    print(ratings)


    #get price of the product
    prices=box.find_all("div",class_="_30jeq3 _1_WHN1")
    for i in prices:
        name = i.text
        prices.append(name)
    print(prices)


# for data in soup.findAll('div',class_='_3pLy-c row'):
#         names=data.find('div', attrs={'class':'_4rR01T'})
#         price=data.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
#         rating=data.find('div', attrs={'class':'_3LWZlK'})
        
        
#         products.append(names.text) # Add product name to list
#         prices.append(price.text) # Add price to list
    
#         ratings.append(rating.text)   #Add rating specifications to list

#printing the length of list
# print(len(products))
# print(len(ratings))
print(len(prices))


import pandas as pd
df=pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings})
df.head(10)


df.to_csv("C:/Users/ANJALI SINGH/OneDrive/Desktop/prodigy/scratch/details.csv")


