# Fibonacci sequence
# 1st number of the sequence is 0
# 2nd number of the sequence is 1
# nth number is the sum of the (n-1)th and (n-2)th numbers
import time
from functools import lru_cache

# Naive solution
# each of fib have two more recursive fib
# imagine it as binary tree
# Time = O(2^n) | Space = O(n)
def getNthFib(n):
    if type(n) != int:
        raise TypeError("n must be a positive int")
    if n < 0:
        raise ValueError("n must be a positive int")

    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:   # n > 2
        return getNthFib(n-1) + getNthFib(n-2)

@lru_cache(maxsize = 35)
def getNthFib2(n):
    if type(n) != int:
        raise TypeError("n must be a positive int")
    if n < 0:
        raise ValueError("n must be a positive int")

    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:   # n > 2
        return getNthFib(n-1) + getNthFib(n-2)

# Memoization solution
# where it's been stored in cache and if in cache, we don't need to recalculate
# imagine this as tree, but if it's in cache, we already have result
# Time = O(n) | Space = O(n)
def getNthFib3(n, memoize = {1: 0, 2: 1}): # memoize store 2 base cas
    
    if n in memoize:
        for key, value in memoize.items():
            print(key, ':', value)
        return memoize[n]
    else:
        memoize[n] = getNthFib3(n -1, memoize) + getNthFib3(n -2, memoize)  
        return memoize[n]
# for i in range(1, 35):
#     print(i, ":", getNthFib(i))
for i in range(1, 35):
    print(i, ":", getNthFib2(i))
# for i in range(1, 100):
#     print(i, ":", getNthFib3(i))

# iterative solution
# array of the last two of fib number or two variable
# Time = O(n) | Space = O(1) 
def getNthFib4(n):
    # getNthFib(1) the only case where we don't to return lastTwo[1]
    # we want to return lastTwo[0]
    lastTwo = [0, 1]
    counter = 3
    while counter <= n:
        nextFib = lastTwo[0] + lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = nextFib
        counter += 1
    return lastTwo[1] if n > 1 else lastTwo[0]

# for i in range(0, 1000):
#     print(i, ":", getNthFib4(i))