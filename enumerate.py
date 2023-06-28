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

# set comprehension 的 word: idx 用法
list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
words1 = {word: idx for idx, word in enumerate(list1)}
# {'Shogun': 0, 'Tapioca Express': 1, 'Burger King': 2, 'KFC': 3}
