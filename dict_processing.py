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

# filter dictionary by values
d = {'sour': 1, 'is': 2, 'sweet': 1, 'this': 2, 'apple': 2}
[key for key, value in d.items() if value == 1]
# ["sour","sweet"]

# Map list from dictionaries
# https://stackoverflow.com/questions/36329412/map-list-from-dictionaries
map_dict = {"a":1, "b":2, "c":6}
list_to_be_mapped  = ["a","a","b","c","c","a"]
list(map(map_dict.get, list_to_be_mapped))
# [1, 1, 2, 6, 6, 1]

# delete key
del d[key]
