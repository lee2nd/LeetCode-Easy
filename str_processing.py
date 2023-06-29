# Remove non-alphanumeric characters from a string
re.sub(r'[\W_]', '', s)

# Lowercase a string
s.lower()

# reverse a string
s[::-1]

# find the index of is
text = 'Python is fun'
result = text.index('is')
print(result)
# Output: 7

# split
"sadbutsad".split("sad")
# ['', 'but', '']

# string 打散
s = "xyz"
print([*s])
# ['x', 'y', 'z']

# removing 1st appearance string
mystring = "Description: Mary had a little lamb Description: "
print(mystring.replace("Description: ","",1))
# "Mary had a little lamb Description: "

# count the occurrences of multiple and different letters within a string
import collections
a = "example"
counter = collections.Counter(a)
print(dict(counter))
# {'e': 2, 'x': 1, 'a': 1, 'm': 1, 'p': 1, 'l': 1}

# filter all index of letter occurrences in string
import re
print([(m.start(0)) for m in re.finditer("a", "banana")])
# [1, 3, 5]

# get unique letter to do the loop stuff
set("aabc")
# {'a', 'b', 'c'}

# find first occurence index
s = "aabc"
s.find("a")
# 0
s.find("d")
# -1
s.index("d")
# ValueError: substring not found

# delete character at specific index in string
myStr = 'apple'
index = 3
myStr[:index] + myStr[index+1:]
 # appe
