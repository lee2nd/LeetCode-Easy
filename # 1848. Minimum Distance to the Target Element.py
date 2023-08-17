class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        return min([abs(idx-start) for idx, num in enumerate(nums) if num == target])
