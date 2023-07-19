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
