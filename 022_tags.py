from bs4 import BeautifulSoup


def read_file():
    file = open('intro_to_soup_html.html')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(),'lxml')


# Accessing tags

meta = soup.meta
print(meta)

# tag methods
'''

name
-- attributes
.get() method
dictionary

'''
print(meta.get('charset'))
# or
print(meta['charset'])

# modify attributes

body = soup.body

body['style'] = 'some style'
print(body)

'''
 Multi valued attributes

'''


print(body['class'])