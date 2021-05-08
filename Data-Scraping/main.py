import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import randint
import pandas as pd

# Retrieve data from ulta 
firstProduct = 0
showPerPage = 50
call = 1
keepGoing = True
# Loop through the total amount of products 
while call <= 100 and keepGoing:
    keepGoing = False
    call += 1
    URL = 'https://www.ulta.com/makeup-lips?N=26yq&No='+ str(firstProduct) +'&Nrpp=' + str(showPerPage)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    products = soup.find_all('div', class_='productQvContainer')
    sleep(randint(2, 10))
    print(page)
    # open a csv file 
    with open("product_data.csv", "a") as csv_file:
        writer = csv.writer(csv_file)
        for eachProduct in products: 
            keepGoing = True 
            # define all classes needed for the products 
            brand = eachProduct.find('h4', class_='prod-title')
            price = eachProduct.find('span', class_='regPrice')
            productType = eachProduct.find('p', class_='prod-desc')
            rating = eachProduct.find('label', class_='sr-only')
            if None in (brand, price, productType, rating):
                continue
            # write data to csv file and strip the text 
            writer.writerow([brand.text.strip(), price.text.strip(), productType.text.strip(), rating.text.strip()])
        firstProduct = firstProduct + showPerPage
    