import re



# ^ character   -- says that the string should start with
regex = re.compile('^abc')
# print(regex.match('abcd'))

# | character -- is the or operator

regex = re.compile('a|b')

# print(regex.match('bd'))

# $ character -- matches the end of line

regex = re.compile('abc$')
# print(regex.match('abc'))

