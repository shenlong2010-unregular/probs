def singleNumber(nums):
    x = 0
    for i in nums:
        x ^= i
    return x

# print(singleNumber([4, 1, 2, 1, 2]))
# print(singleNumber([-1, -1, -2]))

x = 5
y = 2
print(x << y)   # x * 2 ** y
print(x >> y)   # x // 2 ** y
print(x & y)
x = 4
y = 1
print(x & y)
print(x | y)
print(~x)       # -x - 1
print(x ^ y)