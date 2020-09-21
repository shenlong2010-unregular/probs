# O(n) time, O(1) space
def balancedStringSplit(s):
    maxCount = 0
    count = 0
    for i in s:
        if i == 'L':
            count += 1
        elif i == 'R':
            count -= 1

        if count == 0:
            maxCount += 1
    return maxCount
  
print(balancedStringSplit("RLRRLLRLRL"))