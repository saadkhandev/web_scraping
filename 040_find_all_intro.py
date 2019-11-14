from bs4 import BeautifulSoup



def read_file():
    file = open('024_three_sisters.html')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(),'lxml')

# Signature: find_all(name, attrs, recursive, string, limit, **kwargs)

# name parameter


# regex object - string - True - function

a_tags = soup.find_all('a')
# print(a_tags)
for a in a_tags:
    # print(a)
    pass
# attrs parameter

# dicitonary

attr = {'class':'sister'}
first_a = soup.find_all('a', attrs=attr)
# print(first_a)


# limit parameter

a_tags = soup.find_all('a',limit=1)
print(a_tags)