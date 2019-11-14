from bs4 import BeautifulSoup
import re


def read_file():
    file = open('consumer_reports.txt')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(),'lxml')
products = {}   # product name - key product link - value


product_names = [div.a.string.strip() for div in soup.find_all('div',class_='crux-body-copy')]
print(product_names)

product_links = [f"https://www.consumerreports.org/{div.a['href'].strip()}" for div in soup.find_all('div',class_='crux-body-copy')]
print(product_links)

products = {div.a.string.strip():f"https://www.consumerreports.org/{div.a['href'].strip()}" for div in soup.find_all('div',class_='crux-body-copy')}

for key,value in products.items():
    print(key , '   -->',value)
    pass
