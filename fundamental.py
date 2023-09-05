# infinite number
# ∞
float("inf")
# -∞
float(-inf)

# assigning multiple values in an inline if/else statement
# https://stackoverflow.com/questions/67277134/assigning-multiple-values-in-an-inline-if-else-statement
x = y = 0
value = 11
threshold = 5
x, y = (x+1, 0) if value <= threshold else (x-1, value)
x
# -1
y
# 11

"A".isalpha()
True
"-".isalpha()
False

s = [1,3,3,2,5]
# 以下兩個跑出來的結果一樣
sorted(list(set(s)))
sorted(set(s))
# [1,2,3,5]

"A".swapcase()
# a
"a".swapcase()
# A

s0 = "abc"
s1 = "derfg"
max(s0,s1,key=len)
# 'derfg'

# 迴圈夾擠
for i in range(10):
    print((i,~i))
# (0, -1)
# (1, -2)
# (2, -3)
# (3, -4)
# (4, -5)
# (5, -6)
# (6, -7)
# (7, -8)
# (8, -9)
# (9, -10)  
