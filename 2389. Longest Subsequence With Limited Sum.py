# 用到 accumulate, bisect_right 觀念

# https://www.educative.io/answers/what-is-the-itertoolsaccumulate-method-in-python
from itertools import accumulate
lst = [1,2,3,4,5, 5, 6, 6]
print("Originl list - ", lst)
print("Sum accumulation - ", list(accumulate(lst)))
# Originl list -  [1, 2, 3, 4, 5, 5, 6, 6]
# Sum accumulation -  [1, 3, 6, 10, 15, 20, 26, 32]

# https://www.educative.io/answers/what-is-bisectbisectright-in-python
# 裡面放的 list 必須是已經排序過

import bisect
nums = [1,3,5,7,10,25,49,55]
ele = 25

#get index where to insert the element
idx = bisect.bisect_right(nums, ele)
print(f"bisect_right index {idx}")

idx = bisect.bisect_left(nums, ele)
print(f"bisect_left index {idx}")

# bisect_right index 6
# bisect_left index 5

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums = list(accumulate(sorted(nums)))
        return [bisect_right(nums, q) for q in queries]
