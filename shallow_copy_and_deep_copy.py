# https://www.programiz.com/python-programming/shallow-deep-copy

# example 1 : using "=" operator, 改一個，兩個都變，記憶體位置相同
old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
new_list = old_list

old_list.append([4, 4, 4])

print("Old list:", old_list)
print("New list:", new_list)
# Old list: [[1, 2, 3], [4, 5, 6], [7, 8, 'a'], [4, 4, 4]]
# New list: [[1, 2, 3], [4, 5, 6], [7, 8, 'a'], [4, 4, 4]]

new_list[2][2] = 9
print('Old List:', old_list)
print('New List:', new_list)
# Old List: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# New List: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# example 2 : using shallow copy, 改一個，兩個都變，記憶體位置相同，但用 append 就有差別
import copy
old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.copy(old_list)
old_list.append([4, 4, 4])

print("Old list:", old_list)
print("New list:", new_list)
# Old list: [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]]
# New list: [[1, 1, 1], [2, 2, 2], [3, 3, 3]]

old_list[1][1] = 'AA'
print("Old list:", old_list)
print("New list:", new_list)
# Old list: [[1, 1, 1], [2, 'AA', 2], [3, 3, 3]]
# New list: [[1, 1, 1], [2, 'AA', 2], [3, 3, 3]]

# example 3 : using deep copy, 改一個，另一個不變，記憶體位置不同
import copy
old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)
old_list[1][0] = 'BB'

print("Old list:", old_list)
print("New list:", new_list)
# Old list: [[1, 1, 1], ['BB', 2, 2], [3, 3, 3]]
# New list: [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
