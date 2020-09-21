import re
from collections import Counter
password = "Hello@$World19"
checkNum = Counter(map(str.isdigit, password)) # return 2 True
def evaluatePassword(s):
    special_check = re.compile('[!@#$%&*]')
    number_check = re.compile('[0-9]')
    # print(re.findall(special_check, s))
    # print(re.findall(number_check, s))
    if len(s) >= 7 and \
        len(re.findall(special_check, s)) >= 2 and \
        len(re.findall(number_check, s)) >= 2:
        return 'Strong'
    else:
        return 'Weak'

# naive solution
def evaluatePassword1(s):
    countS = 0
    countN = 0
    for char in s:
        if char in '!@#$%&*]':
            countS += 1
        elif char.isdigit():
            countN += 1

    return 'Strong' if countN >= 2 and countS >= 2 and len(s) >=7 else 'Weak'

print(evaluatePassword1(password))
print(evaluatePassword(password))

