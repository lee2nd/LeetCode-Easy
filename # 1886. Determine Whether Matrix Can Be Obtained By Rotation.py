class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4): 
            if mat == target: return True
            mat = [list(x) for x in zip(*mat[::-1])]
        return False 

# https://stackoverflow.com/questions/8421337/rotating-a-two-dimensional-array-in-python

# 1. [::-1] - makes a shallow copy of the original list in reverse order. Could also use reversed() which would produce a reverse iterator over the list rather than actually copying the list (more memory efficient).
# 2. * - makes each sublist in the original list a separate argument to zip() (i.e., unpacks the list)
# 3. zip() - takes one item from each argument and makes a list (well, a tuple) from those, and repeats until all the sublists are exhausted. This is where the transposition actually happens.
# 4. list() converts the output of zip() to a list.
