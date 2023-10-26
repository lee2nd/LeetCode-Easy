# https://docs.python.org/3/library/itertools.html

import itertools

for i,j in itertools.product(range(3), range(3)):
    print(i,j)

# 0 0
# 0 1
# 0 2
# 1 0
# 1 1
# 1 2
# 2 0
# 2 1
# 2 2

product('ABCD', repeat=2)
# AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD

# 排列
permutations('ABCD', 2)
# AB AC AD BA BC BD CA CB CD DA DB DC

# 組合
combinations('ABCD', 2)
# AB AC AD BC BD CD

combinations_with_replacement('ABCD', 2)
# AA AB AC AD BB BC BD CC CD DD
