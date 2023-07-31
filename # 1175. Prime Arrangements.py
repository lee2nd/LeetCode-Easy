# 計算階層
# https://www.delftstack.com/zh-tw/howto/python/python-factorial/
def factorial(n): 
    return 1 if (n==1 or n==0) else n * factorial(n - 1);   
num = 5; 
print("Factorial of",num,"is", factorial(num))
# 120

# Modulo 10^9+7 (1000000007)
# https://www.geeksforgeeks.org/modulo-1097-1000000007/
num = 384819794120128945611437497519917684079008569815424637369583735441344644079427866367657953100203395372827017216000000000000000000000000
num%1000000007
# 682289015
