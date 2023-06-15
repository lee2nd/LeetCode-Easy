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
