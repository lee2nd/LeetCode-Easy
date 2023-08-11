# my solution
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(acc) for acc in accounts])  
      
# 優話寫法, max 可以直接包 list comprehension
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(acc) for acc in accounts)
