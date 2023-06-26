# 知識點
# 1. 
x = [[1,0]]
x[0][0]
# 1
x[-1][0]
# 也是1 (因為-1也是最後一個的意思)

# 2. 二維陣列全部元素之和
sum([sum(sublist) for sublist in my_list])

# 3.if 用 and 串聯多個條件，前者會優先跑，以下兩個 code 在做 index +1 時會 out of range 的差異
# Wrong
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 1:
            if grid[i][j-1] == 1 and j-1>=0:
                count+=1
            if grid[i][j+1] == 1 and j+1<len(grid[i]):
                count+=1
            if grid[i-1][j] == 1 and i-1>=0:
                count+=1
            if grid[i+1][j] == 1 and i+1<len(grid):
                count+=1  
# Right
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 1:
            if grid[i][j-1] == 1 and j-1>=0:
                count+=1
            if j+1<len(grid[i]) and grid[i][j+1] == 1:
                count+=1
            if grid[i-1][j] == 1 and i-1>=0:
                count+=1
            if i+1<len(grid) and grid[i+1][j] == 1:
                count+=1  
