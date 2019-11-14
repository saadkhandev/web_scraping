from bs4 import BeautifulSoup



def read_file():
    file = open('024_three_sisters.html')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(),'lxml')

# .parents              --- returns a list ( generator )  of parents

link = soup.a
# print(link.parent.name)
#
for parent in link.parents:
    print(parent.name)
