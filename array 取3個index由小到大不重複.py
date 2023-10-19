for i in range(5):
    for j in range(i+1,5):
        for k in range(j+1,5):
            print(i,j,k)

# 0 1 2
# 0 1 3
# 0 1 4
# 0 2 3
# 0 2 4
# 0 3 4
# 1 2 3
# 1 2 4
# 1 3 4
# 2 3 4    

# 2873. Maximum Value of an Ordered Triplet I

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    ans = max(ans,(nums[i] - nums[j]) * nums[k])
        return ans
