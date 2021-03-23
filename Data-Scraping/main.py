import requests
from bs4 import BeautifulSoup


# retrieve data from ulta 
URL = 'https://www.ulta.com/makeup-lips?N=26yq'
page = requests.get(URL)

# after installing/importing beautiful soup allows to take html and parse as needed 
soup = BeautifulSoup(page.content, 'html.parser')

# find the container for all the variables 

results = soup.find(id='search-prod')
print(results.prettify())

make_up_elems = results.find_all('li', class_= 'productQvCcontainer')

# for make_up_elems in make_up_elems:
#     make_up_brand = make_up_elems.find('h4', class_ 'brand')
#     make_up_name = make_up_elems.find('p', class_'name')