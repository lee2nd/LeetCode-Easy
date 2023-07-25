# https://www.runoob.com/python/python-func-divmod.html
# return (a//b, a%b)

divmod(7, 2)
# (3, 1)
divmod(8, 2)
# (4, 0)
divmod(1+2j,1+0.5j)
# ((1+0j), 1.5j)

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        for i in range(len(num) - 1, -1, -1):
            k, num[i] = divmod(num[i] + k, 10)
        while k:
            k, a = divmod(k, 10)
            num = [a] + num
        return num
