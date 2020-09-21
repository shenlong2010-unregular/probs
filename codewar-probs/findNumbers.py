#O(n) time, O(n) space
def findNumbers(nums):
    return len([i for i in nums if len(str(i)) % 2 == 0])

#O(n) time, O(n) space
def findNumbers1(nums):
    count = 0
    for i in range(len(nums)):
        if len(str(nums[i])) % 2 == 0:
            count += 1  
    return count

print(findNumbers1([12,345,2,6,7896]))