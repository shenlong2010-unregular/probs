import inspect
# time: O(n^2) | space: O(1)
def twoNumberSum1(array, targetSum):

    for i in range(len(array)-1): # iterate to the before end of the loop, 0 - 7
    # for i in range (len(array)) can be used but in second loop the last index will not compare to anything
    # or basically comparing with last index of second loop - redundancy

        firstNum = array[i]
        # print(i, end = ' ')
        # print(firstNum)

        for j in range(i + 1, len(array)):
            secondNum = array[j]
            # print(j, end = ' ')
            # print(secondNum)
            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum]
    return []
# time: O(n) | space: O(n) 
def twoNumberSum2(array, targetSum):
    myhash = {} # hashtable
    for x in array:
        # y = targetSum - x
        # print(x)
        # print(y) 
        if (targetSum - x) in myhash:
            return [targetSum - x, x]
        else:
            myhash[x] = True 
            # print(myhash)
    return []

def twoNumberSum3(array, target):
    array.sort()
    # print(array)
    left = 0
    right = len(array) - 1
    while left < right:
        sum = array[left] + array[right]
        print(sum)
        if sum == target:
            return (array[left], array[right])
        elif sum < target:
            left += 1
            print("left", left, array[left])
        else:
            right -= 1
            print("right", right, array[right])
    return []

if __name__ == "__main__":
    # new_list = int(input()).split()
    # sum = int(input())
    arr = [3, 5, -4, 8, 11, 1, -1, 6]
    # print(len(arr) -1)
    print(twoNumberSum1(arr, 10))
    print(twoNumberSum2(arr, 10))
    print(twoNumberSum3(arr, 15))
    