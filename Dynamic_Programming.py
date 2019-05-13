"""
Fibonnaci using -only RECURSION

"""

def fib(n):
    if n == 1 or n == 2 :
        result = 1
    else:
        result = fib(n-1) + fib(n-2)  # the sum of the two previous fibonacci numbers
    return result

print(fib(5))


"""
solution works but it's very inefficient 

time it takes grows exponentially as in o(2^n)
"""


"""
Fibonacci sequence - USING MEMOIZATION 


"""

def fib_2(n,memo):
    if memo[n] is not None:   # checking if memo is not null, if its not = to null that means that we've alredy seen it
        return memo[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib_2(n-1, memo) + fib_2(n-2,memo)
    memo[n] = result
    return result

def fib_memo(n):
    memo = [None] * (n+1)
    return  fib_2(n,memo)

print(fib_memo(100))



"""
Time complexity for this solution will be : with n possible arguments due to argument n . 
total = 2n + 1 
result = 0(1)
"""


"""
BOTTOM UP APPROACH

"""
def fib_bottom_up(n):
    if n == 1 or n == 2:
        return 1
    bottom_up = [None]*(n + 1)
    bottom_up[1]=1
    bottom_up[2]=1
    for i in range(3,n+1):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i -2]
    return bottom_up[n]

print(fib_bottom_up(1000))
"""
Time complexity  : o(n)
"""
