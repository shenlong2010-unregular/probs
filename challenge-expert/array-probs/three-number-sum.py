# O(n^3) T, O(n) S
def threeNumberSum1(array, targetSum):
    array.sort()
    count = 0
    lst = []
    for x in range(len(array)-2):
        first = array[x]
        for y in range(x + 1, len(array)-1):
            second = array[y]
            for z in range(y + 1, len(array)):
                third = array[z]

                if first + second + third == targetSum:
                    count += 1
                    lst.append(([first, second, third]))
    return lst

print(threeNumberSum1([12, 3, 1, 2, -6, 5, -8, 6], 0))

#
def threeNumberSum2(array, targetSum):
    nums = {}
    pass

# O(n^2) T, O(n) S
# sorting would not effective the time complexity
# even if we use the most efficient sort
# such as merge | quick sort O(nlogn)
# O(n^2) > O(nlogn), therefore O(n^2) T
def threeNumberSum3(array, targetSum):
    lst = []
    array.sort()
    for i in range(len(array) - 2):
        left = i + 1   # index right next to i
        right = len(array) - 1  # far end of the array
        while left < right:
            currentSum = array[i] + array[left] + array[right]
            if currentSum == targetSum:
                lst.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif currentSum < targetSum:
                left += 1
            elif currentSum > targetSum:
                right -= 1
    return lst
    

print(threeNumberSum3([12, 3, 1, 2, -6, 5, -8, 6], 0))
