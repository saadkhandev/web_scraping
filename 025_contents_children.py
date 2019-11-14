from bs4 import BeautifulSoup



def read_file():
    file = open('024_three_sisters.html')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(),'lxml')



# tag.contents         -- returns a list of children

# head = soup.head
# print(head.contents)
# for child in head.contents:
#     print(child if child is not None else '')

body = soup.body
#
#

for child in body.contents:
    # print(child if child is not None else '',end='\n\n\n\n')
    pass





# .children         -- returns an iterator
print(type(body.children))
print(type(body.contents))

for child in body.children:
    # print(child if child is not None else '', end='\n\n\n\n')
    pass