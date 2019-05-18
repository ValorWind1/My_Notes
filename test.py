"""

fibonacci Dynamic programming memoization
"""


def fib ( n,memo):
    if memo[n] is not None:
        return memo[n]
    if  n==1 or n==2:
         result =1
    else:
            result = fib(n-1,memo) + fib(n-2,memo)
    memo[n] = result
    return result

def memo(n):
    memo=[None] * (n+1)
    return  memo


"""
fibaonnaci dynamic programming bottom up approach 
"""

def fib (n):
    if n ==1 or n ==2 :
        return 1
    bottom_up = [n]
    bottom_up[1]=[1]
    bottom_up[2]=[1]

    for i in range (3,n+1):
        bottom_up[i] = bottom_up[n-1] + bottom_up[n-2]
    return bottom_up[n]
    