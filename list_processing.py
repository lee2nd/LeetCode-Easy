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
