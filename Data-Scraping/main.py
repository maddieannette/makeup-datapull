import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import randint
import numpy as np
import pandas as pd

# retrieve data from ulta 
firstProduct = 0
showPerPage = 50
call = 1
keepGoing = True
while call <= 100 and keepGoing:
    keepGoing = False
    call += 1
    URL = 'https://www.ulta.com/makeup-lips?N=26yq&No='+ str(firstProduct) +'&Nrpp=' + str(showPerPage)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    products = soup.find_all('div', class_='productQvContainer')
    sleep(randint(2, 10))
    print(page)
    for eachProduct in products: 
        keepGoing = True 
        brand = eachProduct.find('h4', class_='prod-title')
        price = eachProduct.find('span', class_='regPrice')
        productType = eachProduct.find('p', class_='prod-desc')
        if None in (brand, price, productType):
            continue
        print(brand.text.strip())
        print(price.text.strip())
        print(productType.text.strip())
        print()
    firstProduct = firstProduct + showPerPage
        
        
# allProducts = pd.DataFrame(
# {
#     "Brand": brand,
#     "Price": price,
#     "Name": productType,
# })
# print(allProducts)
# allProducts.to_csv(r"/Users/madelineflores/Documents/allproducts.csv", index="False", header="True" )


# after installing/importing beautiful soup allows to take html and parse as needed 
# soup = BeautifulSoup(page.content, 'html.parser')


# # find the container for all the variables 

# product = soup.find_all('div', class_='productQvContainer')

# for eachProduct in product: 
#     brand = eachProduct.find('h4', class_='prod-title')
#     price = eachProduct.find('span', class_='regPrice')
#     productType = eachProduct.find('p', class_='prod-desc')
#     if None in (brand, price, productType):
#         continue
#     print(brand.text.strip())
#     print(price.text.strip())
#     print(productType.text.strip())
#     print()