# Small observation that the sequence of index is [0,1,2,3..],
# if we get its module by 2, we get [0,1,0,1,0..],
# which is the alternating binary sequence we want.

# So we iterate the string,
# check if the characters[i] is same as the i % 2.
# Note that s[i] is a character,
# and s[i] - '0' making it to integer.

# We accumulate the number of difference,
# which is the number of operation to make it into 01 string.

# We can do the same to find out res,
# the number of operation for 10 string.
# But we don't have to,
# becaue this equals to s.length - res.

# 出來的結果只有可能是 "01010101...." 或是 "10101010...."，取轉換次數最少的那個
class Solution:
    def minOperations(self, s):
        res = sum(i % 2 == int(c) for i, c in enumerate(s))
        return min(res, len(s) - res)
