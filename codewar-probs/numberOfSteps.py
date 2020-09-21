# O(n) time | O(1) space
def numberOfSteps (num: int) -> int:
    step = 0
    while num != 0:
        if num % 2 == 0:
            num /= 2
            step += 1
        elif num % 2 != 0:
            num -= 1
            step += 1
    return step

print(numberOfSteps(num = 14))