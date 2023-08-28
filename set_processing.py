# Initialize a Python set
set()

# Quick Examples of Joining Two Sets
# Join using |
myset = myset1 | myset2 | myset3

# Join using union()
myset = myset1.union(myset2,myset3)

# check if subset in in set
{1,2} <= {4,1,2}
# True
{1,5} <= {4,1,2}
# False

# append values to a set
a.add(1)
a.add(2)
a.update([3, 4])
# {1, 2, 3, 4}

# remove values to a set
myset.remove("1")

# set 相加
s = {'g', 'e', 'e', 'k', 's'}
t = ('f', 'o')
l = ['a', 'e']
 
s.add(t)
s.update(l)
# {'a', 'g', 'k', 'e', ('f', 'o'), 's'}

# difference
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
# 兩者結果一樣
x.difference(y)
x-y
