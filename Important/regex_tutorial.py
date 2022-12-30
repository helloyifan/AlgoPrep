import re

names = [   
    'Finn bindeballe',
    'Geir Anders Berge',
    'HappyCodingRobot',
    'Ron Cromberge',
    'Sohil']

print('----------------')

# Find people with first and last name only
regex = '^\w+\s+\w+$'
for name in names:
    result = re.search(regex, name)
    if result:
        print(name) # print the name that evaluates to true
        print(result) # prints the "match" object

print('----------------')

# Search for word char sequence starting with C
regex2 = 'C\w*'
for name in names:
    match = re.search(regex2, name)
    if match:
        print(name)
        print(match.start()) #start index where match occurs
        print(match.end()) # end index where match occurs
        print(match.span()) # For convenience, you can retrieve both indices with a single call to the span() method.
        print(match.group()) #  If you want to display the substring that matched the regex, you call the group() method.


print('----------------')

names2 = [
    'Brian Daugette',
    'Veronica Supersonica',
    'Tony Gasparovic',
    'Patrick Germann',
    'm!sha'
]

print('----------------')

# Test for first name and last name with groups by index (starting at index 1)
regex3 = '^(\w+)\s+(\w+)$'
for name in names2:
    match = re.search(regex3, name)
    if match:
        print(match.group(1), match.group(2))

print('----------------')

# For readability we can name groups
regex4 = '^(?P<fn>\w+)\s+(?P<ln>\w+)$' #first group name fn, second ground name ln
for name in names2:
    match = re.search(regex4, name)
    if match:
        print(match.group('fn'), match.group('ln'))

print('----------------')

regex5 = '^[a-zA-Z!]+$'
for name in names2:
    if re.search(regex5, name):
        print(name)

# Scan for blocks of lower case letters
regex6 = '[a-z]+'
for name in names2:
    matches = re.findall(regex6, name)
    if matches:
        print(matches) #returns a list of string instead of match objects

print('----------------')

regex7 = '[a-z]+'
for name in names2:
    matches = re.finditer(regex7, name)
    if matches:
        print(matches) #returns a list of match objects


values = [
    'https://www.socratica.com',
    'http://www.socratica.com',
    'file://test.this.path',
    'com.socratica.www_https://'
]


print('----------------')

## Test if string starts with http or https
regex8 = 'https?' #we are saying 's' can occur 0 or 1 time

for value in values:
    if re.match(regex8, value):
        print(value)


regex9 = 'https?://w{3}.\w+.(org|com)' 
# breaking it down
# starts with http or https, 
# has 3 'w' 
# has 1 or more \w (word characters)
# has org or com

for value in values:
    if re.fullmatch(regex9, value):
        print(value)


