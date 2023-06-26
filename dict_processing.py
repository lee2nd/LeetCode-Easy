# 把一個 list 當成 dict 的 keys
d = {}
for i in keyList:
    d[i] = None

# 取得擁有最大 value 的那個 key
ages = {
    'Matt': 30,
    'Katie': 29,
    'Nik': 31,
    'Jack': 43,
    'Alison': 32,
    'Kevin': 38
}

max_value = max(ages, key=ages.get)
print(max_value)
# Jack

# keys count
len(ages)
# 6
