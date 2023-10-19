# range(大num,小num) 不會報錯, 只是會是空的, 不會有 loop 跑
# key code: a,b,c,d = map(int, str(i))

class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:

        ans  = len([n for n in range(11,100,11)
                                    if low <= n <= high])   # <-- a)

        for i in range(max(1001, low),min(high+1,10000)):   # <-- b)            
            a,b,c,d = map(int, str(i))

            ans+= a+b == c+d

        return ans
