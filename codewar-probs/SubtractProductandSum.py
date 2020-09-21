# import numpy as np
from functools import reduce
# O(n) space, time
def subtractProductAndSum(n):
    num = list(str(n))
    sum = 0
    product = 1
    for i in range(len(num)):
        sum += int(num[i])
        product *= int(num[i])
        
    return product - sum

# O(n) space / O(n) time
def subtractProductAndSum1(n):
    a = [int(x) for x in str(n)]
    return reduce((lambda x, y: x * y), a) - reduce(lambda x, y: x + y, a)

# def subtractProductAndSum2(n):
#     a = [int(x) for x in str(n)]
#     return np.prod(a) - np.sum(a)

def subtractProductAndSum3(n):
    sum = 0
    product = 1
    while n > 0:
        sum += n%10
        product *= n%10

        n //= 10
    return product - sum
print(subtractProductAndSum1(4421))
print(subtractProductAndSum3(4421))