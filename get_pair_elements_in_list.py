#  get each pair of adjacent elements in a list

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(len(my_list) - 1):
    pair = (my_list[i], my_list[i+1])
    print(pair)
