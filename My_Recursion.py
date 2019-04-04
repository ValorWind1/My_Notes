# Recursion, The fibonacci sequence and memoization

def fibonacci(n): #def fibonacci(n). the (n) its the single input n , because this function will return the Nth term.

    if n ==1: # we begin by handling the starting cases.
        return 1  # we return the first term
    elif n == 2:
        return 1 # we return the second term
    elif n > 2: # if n its bigger than 2 we return the sum of the previous 2 terms.
        return fibonacci(n-1) + fibonacci(n-2) # its calling itself . this is a recursive function


# tester
# print the first 10 terms
for n in range(1,11):
    print(n, ":", fibonacci(n)) # this works but will return too slow when int increases, due to useless repetition
                                # Therefore we use Memoization
                                # Memoization : stored the values for recent function calls, so future calls wont have to
                                # repeat the work. idea: cache values.

# Memoization comes in 2 forms . 1- explicitly , and 2- builtin python tool
# we start by creating a dictionary.
fibonacci_cache ={}

def fibonacciMx(n):
    # if we have cached the value, then return it.( if we have n in our cache)
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    # otherwise Compute the Nth term
    if n ==1:
        return 1
    elif n==2:
        return 1
    elif n > 2:
        value = fibonacciMx(n-1) + fibonacciMx(n-2)
    # Cache the value and return it
    fibonacci_cache[n] = value
    return value

# Tester with memoization

for n in range(1,1001):
    print(n, ":",fibonacciMx(n))

# third way python built in tool , using the first function

from functools import lru_cache    # Least , Recently , Used , Cache provides a 1 line way to add memoization to our functions

@lru_cache(maxsize = 1000)  # this is how we call the python tool
def fibonacciPt(n):
    # Check that the input is a positive integer
    if type(n) != int:
        raise TypeError("n must be a positive int")
    if n < 1:
        raise ValueError("n must be a positive int")   # this are helpful error messages.


    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacciPt(n-1) + fibonacciPt(n-2)

# tester for memoizstion python tool

for n in range(1,501):
    print(n,":",fibonacciPt(n))

    # how to calculate the ratio between consecutive terms.
    # print (fibonacciPt(n+1)/ fibonacciPt(n))
for n in range(1,51):
    print(fibonacciPt(n + 1) / fibonacciPt(n))  # golden ration