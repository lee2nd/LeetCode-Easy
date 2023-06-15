# https://realpython.com/python-reduce-function/
# 

# function
functools.reduce(function, iterable[, initializer])

def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value
  
# application
from functools import reduce

def my_add(a, b):
     result = a + b
     print(f"{a} + {b} = {result}")
     return result
  
numbers = [0, 1, 2, 3, 4]
reduce(my_add, numbers)
# 0 + 1 = 1
# 1 + 2 = 3
# 3 + 3 = 6
# 6 + 4 = 10
# 10
