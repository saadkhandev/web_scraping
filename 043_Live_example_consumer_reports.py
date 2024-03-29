from bs4 import BeautifulSoup
import re


def read_file():
    file = open('consumer_reports.txt')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(),'lxml')

all_divs = soup.find_all('div',attrs={'class':'crux-body-copy'})

# for div in all_divs:
#     print(div.a.string.strip())
products = [div.a.string.strip() for div in all_divs]
# print(products)
for product in products:
    print(product)
