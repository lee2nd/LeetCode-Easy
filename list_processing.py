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

# shortest list by length
words = sorted(words, key=len)

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

# 2d
a = [[0,0,0]]*3 
a[0][0] += 1
# [[1, 0, 0], [1, 0, 0], [1, 0, 0]]
# 這是因為在 Python 中，當使用 * 運算符創建一個列表時，實際上是在記憶體中創建了一個對原始列表的引用，而不是創建了三個獨立的列表。因此，當您修改其中一個列表的元素時，由於它們實際上都是對同一個列表的引用，其他所有列表也會反映這個更改

a = [[0, 0, 0] for _ in range(3)]
a[0][0] += 1
# [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
# 這樣就會創建三個獨立的列表，並且您可以單獨修改其中一個列表的元素而不影響其他列表。例如，您可以通過以下方式將第一個列表的第一個元素增加1

# check if all values in list are greater than a certain number
my_list = [30, 34, 56]
all(i >= 30 for i in my_list)
# True

# finding last index of some value in a list
len(verts) - 1 - verts[::-1].index(value)

# delete element in list (don't need to assign to new variable)
l.remove(value)
l.pop(idx)

# filter lists by indices
# https://stackoverflow.com/questions/11847491/python-filtering-lists-by-indices
[aList[i] for i in myIndices]

# 找出 list 中出現次數最多次的元素
lst = [1,1,1,2,2,3,3]
max(lst, key = lst.count)
# 1

# list pop assign 值, 原 list 還是會刪 element, assign 的 variable 就會是 pop 掉的那個 element
queue = ['G']
s = queue.pop(0)
queue
# []
s
# 'G'

# filtering a list of strings based on contents
lst = ['a','ab','abc','bac']
list(filter(lambda k: 'ab' in k, lst))
['ab', 'abc']

# insert(index, obj)
l = [1, 2, 3, 0, 0]
l.insert(2,4)
# [1, 2, 4, 3, 0, 0]
