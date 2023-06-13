def square(x) :            
     return x ** 2

list(map(square, [1,2,3,4,5]))
# [1, 4, 9, 16, 25]

my_list = [1, 2, 3, 4, 5]
my_str = ', '.join(map(str, my_list))
print(my_str)  

# "1, 2, 3, 4, 5"
