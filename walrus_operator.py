# https://stackoverflow.com/questions/26000198/what-does-colon-equal-in-python-mean

# without walrus
n = 30
if n > 10:
    print(f"{n} is greater than 10")
    
# with walrus，只需要兩行
if (n := 30) > 10:
    print(f"{n} is greater than 10")

# 重點
# 只有 Python 3.8 可用
# := 就等於 =
# 其實不需要常用
# 使用情境 : regular expressions、要精簡 code 時
