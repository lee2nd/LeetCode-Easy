class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        r = Counter(nums)
        return sorted(nums, key=lambda x: (r[x], -x))

nums = [1, 1, 2, 2, 2, 6, 6, 4, 4, 5, 5, 3]
r = {2: 3,
     1: 2,
     6: 2,
     4: 2,
     5: 2,
     3: 1}

# sort by dictionary values
sorted(nums, key=lambda x: r[x])
# [3, 1, 1, 6, 6, 4, 4, 5, 5, 2, 2, 2]

# 1st sort by dictionary values
# 2nd sort by dictionary keys(ascending)
sorted(nums, key=lambda x: (r[x], x))
# [3, 1, 1, 4, 4, 5, 5, 6, 6, 2, 2, 2]

# 1st sort by dictionary values
# 2nd sort by dictionary keys(descending)
sorted(nums, key=lambda x: (r[x], -x))
# [3, 6, 6, 5, 5, 4, 4, 1, 1, 2, 2, 2]
