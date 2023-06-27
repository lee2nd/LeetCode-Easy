# https://www.geeksforgeeks.org/python-program-to-print-the-fibonacci-sequence/
# https://medium.com/@ryanyang1221/dynamic-programming-explanation-with-fibonacci-%E7%94%A8%E8%B2%BB%E6%B3%A2%E9%82%A3%E5%A5%91%E6%95%B8%E5%88%97%E4%BE%86%E8%A7%A3%E9%87%8B%E5%8B%95%E6%85%8B%E8%A6%8F%E5%8A%83-8ce318601d0f

def climbStairs(n):
    # optimal solution
    if n==0: return 0
    if n==1: return 1
    if n==2: return 2
    dp = [0]*(n+1) # considering zero steps we need n+1 places
    dp[1] = 1
    dp[2] = 2
    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp)
    return dp[n]
  
climbStairs(9)
# [0, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 55

climbStairs(28)
# [0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229]
# 514229

# recursive version (O(2^n))
def recur_fib(n):
   if n <= 1:
       return n
   else:
       return(recur_fib(n-1) + recur_fib(n-2))

# dynamic programming version (O(1))
def dp_fib(n):
    dp_0, dp_1 = 0,1
    for i in range(n):
        dp_0, dp_1 = dp_1, dp_1+dp_0
    return dp_0
