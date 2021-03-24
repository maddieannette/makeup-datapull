import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
from time import sleep
from random import randint
import numpy as np


# retrieve data from ulta 
pages = np.arange(1, 672, 96)
for page in pages:
    URL = 'https://www.ulta.com/makeup-lips?N=26yq'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    product = soup.find_all('div', class_='productQvContainer')
    sleep(randint(2, 10))
    print(page)
    for eachProduct in product: 
        brand = eachProduct.find('h4', class_='prod-title')
        price = eachProduct.find('span', class_='regPrice')
        productType = eachProduct.find('p', class_='prod-desc')
        if None in (brand, price, productType):
            continue
        print(brand.text.strip())
        print(price.text.strip())
        print(productType.text.strip())
        print()
allProducts = pd.DataFrame(
    {
        "Brand": brand,
        "Price": price,
        "Name": productType,
    }
)
print(allProducts)
allProducts.tocs


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



