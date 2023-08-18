# https://stackoverflow.com/questions/464864/get-all-possible-2n-combinations-of-a-list-s-elements-of-any-length

import itertools

stuff = [1, 2, 3]
for L in range(len(stuff) + 1):
    for subset in itertools.combinations(stuff, L):
        print(subset)

# ()
# (1,)
# (2,)
# (3,)
# (1, 2)
# (1, 3)
# (2, 3)
# (1, 2, 3)
