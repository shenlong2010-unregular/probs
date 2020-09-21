# Product Sum Recursion

# Time = O(n) n is NOT the element in the original array
# n is the TOTAL of the array including sub-array and their sub-array
# Space = O(d) d as depth the array

# O(n) time | O(d) space - where n is the totala number of elements in the array,
# including sub-elements, and d is the greatest depth of "special" arrays in the array
def productSum1(array, multiplier = 1):
    sum = 0

    for element in array: # assume array is integer value

        if type(element) is list: # special case where i == list || array
            sum += productSum1(element, multiplier + 1)
        else:
            sum += element
    return sum * multiplier

# print(productSum1([5, 2, [7, -1], 3, [6, [-13, 8], 4]]))
# n is 12 because 1:5, 2:2, 3:[7,-1], 4:7, 5:-1, 6:3,
#                 7:[6, [-13, 8], 4], 8:6, 9:[-13,8],
#                 10:-13, 11:8, 12:4

def productSum2(array):
    sum = 0
    m = 1
    for element in array:
        if type(element) != int:
            sum += productSum2(element)
            m += 1
        else:
            sum += element
    return sum * m
print(productSum2([5, 2, [7, -1], 3, [6, [-13, 8], 4]]))