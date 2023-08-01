# 改成用 extend 的方式會比 append 快很多

class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n % 2 == 1: ans = [0]
        else: ans = []
        for i in range(1,(n//2)+1):
            ans.append(i)
            ans.append(-i)  
        return ans

class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n % 2 == 1: ans = [0]
        else: ans = []
        for i in range(1,(n//2)+1):
            ans.extend([i, -i])
        return ans  
