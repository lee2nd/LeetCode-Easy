# https://stackoverflow.com/questions/7286365/print-a-list-in-reverse-order-with-range

for i in range(3, -1, -1):
    # range(start, stop, step)
    print(i)
    
# 3
# 2
# 1
# 0  

for i in reversed(range(4)):
    print(i)
    
# 3
# 2
# 1
# 0    
