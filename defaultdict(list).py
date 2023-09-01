from collections import defaultdict

d = defaultdict(list)
d["a"] = [1,2,3]
print(d["a"])
# [1,2,3]

d["a"].append(4)
print(d["a"])
# [1, 2, 3, 4]

d["a"].extend([5,6,7])
print(d["a"])
# [1, 2, 3, 4, 5, 6, 7]
