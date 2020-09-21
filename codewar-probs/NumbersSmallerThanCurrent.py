# O(n) ST
def smallerNumbersThanCurrent(nums):
    lst = []
    
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):

            if j != i and nums[j] < nums[i]:
                count += 1
        lst.append(count)
    print(lst)
smallerNumbersThanCurrent([8,1,2,2,3])