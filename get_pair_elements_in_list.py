my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#  get each pair of adjacent elements in a list
for i in range(len(my_list) - 1):
    pair = (my_list[i], my_list[i+1])
    print(pair)
# (1, 2)
# (2, 3)
# (3, 4)
# (4, 5)
# (5, 6)
# (6, 7)
# (7, 8)
# (8, 9)
# (9, 10)    

#  get every combination of 2 elements in a list    
for i in range(len(my_list)):
    for j in range(i+1, len(my_list)):
        pair = (my_list[i], my_list[j])
        print(pair)    
# 共 C10取2 總組合
# (1, 2)
# (1, 3)
# (1, 4)
# (1, 5)
# (1, 6)
# (1, 7)
# (1, 8)
# (1, 9)
# ...
# (7, 9)
# (7, 10)
# (8, 9)
# (8, 10)
# (9, 10)

# the usage of enumerate()    
List = ['a', 'b', 'c', 'd', 'e']        
for index, value in enumerate(List):
    print(index, value)    
# (0, 'a')
# (1, 'b')
# (2, 'c')
# (3, 'd')
# (4, 'e')    
