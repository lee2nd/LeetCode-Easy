# https://www.geeksforgeeks.org/enumerate-in-python/

l1 = ["eat", "sleep", "repeat"]

# creating enumerate objects
obj1 = enumerate(l1)

print(list(enumerate(l1)))
# [(0, 'eat'), (1, 'sleep'), (2, 'repeat')]

# enumerate function in loops
for i, element in enumerate(l1):
    print(i)
    print(element)
# 0
# eat
# 1
# sleep
# 2
# repeat  
