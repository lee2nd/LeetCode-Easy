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

# removing 1st appearance string
mystring = "Description: Mary had a little lamb Description: "
print(mystring.replace("Description: ","",1))
# "Mary had a little lamb Description: "
