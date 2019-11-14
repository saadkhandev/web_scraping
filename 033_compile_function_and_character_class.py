import re



# re.compile(pattern)       -- returns a regex object

regex = re.compile('[+]')
regex_2 = re.compile('[^ a-zA-Z]')



# regex.match(string to match) -- returns None if no match else returns a match object

print(regex_2 .match('1'))



# character class




# complement the set [^pattern]

print(regex.match('+'))


# all metacharacters lose their meaning inside a character class