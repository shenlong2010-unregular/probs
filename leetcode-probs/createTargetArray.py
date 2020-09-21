# O(n) time, O(n) space
def createTargetArray(nums, index):
        indexNums = 0
        indexIndex = 0
        arr = []
        while (indexNums != len(nums)) and (indexIndex != len(index)):
            arr.insert(index[indexIndex], nums[indexNums])
            print(arr)
            indexNums += 1
            indexIndex += 1
        return arr
print(createTargetArray([0,1,2,3,4], [0,1,2,2,1])) # output [0,4,1,3,2]
print(createTargetArray([1,2,3,4,0], [0,1,2,3,0])) # output [0,1,2,3,4]

# O(n^2) SP
def createTargetArray1(nums, index):
    arr = []
    for idx, number in zip(index, nums):
        arr.insert(idx, number)
        return arr
    
#     for k in range(len(nums)):
#         arr.insert(index[k], nums[k])
#         return arr


