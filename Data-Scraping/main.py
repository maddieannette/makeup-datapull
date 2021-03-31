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
    with open("product_data.csv", "a") as csv_file:
        writer = csv.writer(csv_file)
        for eachProduct in products: 
            keepGoing = True 
            brand = eachProduct.find('h4', class_='prod-title')
            price = eachProduct.find('span', class_='regPrice')
            productType = eachProduct.find('p', class_='prod-desc')
            rating = eachProduct.find('label', class_='sr-only')
            if None in (brand, price, productType, rating):
                continue
            # print(brand.text.strip())
            # print(price.text.strip())
            # print(productType.text.strip())
            # writer.writerow([thisBrand, thisPrice, thisProductType])
            writer.writerow([brand.text.strip(), price.text.strip(), productType.text.strip(), rating.text.strip()])
        firstProduct = firstProduct + showPerPage
    