import math
def largest_power(n):
    if n < 4 and n != 1:
        return (1, -1)
    return math.log(n, 2)
print(largest_power(90))