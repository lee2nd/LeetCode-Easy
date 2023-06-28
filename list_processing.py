# remove all occurrences of a value from a list
# https://stackoverflow.com/questions/1157106/remove-all-occurrences-of-a-value-from-a-list
# list.remove(2) 只能一次移掉一個(從最前面開始移)
x = [1,2,3,2,2,2,3,4]
x = [i for i in x if i != 2]
print(x)
# [1, 3, 3, 4]

# shortest string in list
min(['Alice', 'Bob', 'Pete',], key=len)
# 'Bob'

# slice each string in list
list_of_words = ['One', 'Two', 'Three', 'Four', 'Five']
[w[:2] for w in list_of_words]
# ['On', 'Tw', 'Th', 'Fo', 'Fi']

# the most Pythonic way to convert a list of strings to a list of ints
strings = ["1","2","3"]
[int(x) for x in strings] 

# find all occurrences of an element index in a list
my_list = [1,2,3,4,1,2,1,2,3,4]
indices = [i for i, x in enumerate(my_list) if x == 1]
# [0, 4, 6]

# check if a list is empty
lst1 = ["Hire", "the", "top", "1%", "freelancers"]
lst2 = []
if lst2:
    print("list is not empty")
else:
    print("list is empty")

# sort comparison
x = [4, 2, 5, 3, 1]
# x 不會變
y = sorted(x)
# x 會變
x.sort()

# Replace Values in a List
l = ['Hardik', 'Rohit', 'Rahul', 'Virat', 'Pant']
l = list(map(lambda x: x.replace('Pant', 'Ishan'), l))

# Calculate the rank vector of a list
l = [10,3,8,9,4]
[sorted(l).index(x) for x in l]
# [4, 0, 2, 3, 1]

# jump each 2 intervals
l = [1, 7, 2, 14, 4, 28]
l[::2]
# [1, 2, 4]

# count 2 d array total elements
two_d_lst = [[1,2],[3,4]]
sum(len(sub_lst) for sub_lst in two_d_lst)
# 4
