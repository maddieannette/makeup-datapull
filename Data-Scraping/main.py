import requests
from bs4 import BeautifulSoup

# retrieve data from ulta 

def pageturning():
    openPage = open("makeup.text", "w+")
    pageCount = 0 

    while pageCount>= 0:
        pageCount += 1
        urlPage = 'https://www.ulta.com/makeup-lips?N=26yq' + '26yq' + str(pageCount) + '.html'
        refer = urlPage
    try:
            req = urllib.request.Request(url = urlPage, headers=headers)
            response = urlopen(req)
            html = response.read()
        except error,HTTPError as e: 
            break 
        soup = BeautifulSoup(page.content, 'html.parser')
        page = soup.find_all(class_="next")
#counter

def getNextPage(soup):
    page = soup.find('ul', class_='floatr pagination-select')
    if not page.find('li', class_='next'):
        url = 'https://www.ulta.com/' + str(page.find('li', class_='prev')).find('a')['href'])
        return url
    else:
        return

while True:
    soup = getData(url)
    url = getNextPage(soup)
    if not url:
        break 
    print(url)
pages = soup.find_all(class=_'next')

# URL = 'https://www.ulta.com/makeup-lips?N=26yq'
# page = requests.get(URL)
# soup = BeautifulSoup(page.content, 'html.parser')
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