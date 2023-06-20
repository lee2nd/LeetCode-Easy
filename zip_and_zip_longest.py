from itertools import zip_longest

# 兩個 list 長度可不同
x =[1, 2, 3, 4, 5, 6, 7]
y =[8, 9, 10]
z = list(zip_longest(x, y))
# [(1, 8), (2, 9), (3, 10), (4, None), (5, None), (6, None), (7, None)]

# 兩個 list 長度必須相同
name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ]
roll_no = [ 4, 1, 3, 2 ]
mapped = zip(name, roll_no)
list(mapped)
# [('Manjeet', 4), ('Nikhil', 1), ('Shambhavi', 3), ('Astha', 2)]
