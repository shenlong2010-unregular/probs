# A palindrome is defined as a string that is written the same forward and backward
# Time O(n) | Space O(1)
def isPalindrome1(string):
    if string == string[::-1]:
        return True
    return False
# Time O(n) | Space O(1)
def isPalindrome2(string):
    reversedstring = "".join(reversed(string))
    return False if reversedstring != string else True
# Time O(n^2) | Space O(n)
def isPalindrome3(string):
    reversedString = []
    index = len(string)
    while index > 0:
        reversedString += string[index -1]
        index = index - 1
    if ''.join(reversedString) == string:
        return True
    return False
# Time O(n^2) | Space O(n)
def isPalindrome4(string):
    reversedString = []
    index = len(string)
    while index > 0:
        reversedString += string[index -1]
        index = index - 1
    if list(string) == reversedString:
        return True
    return False

# Time O(n^2) | Space O(n)
def isPalindrome5(string):
    new_string = ""
    for char in string:
        new_string = char + new_string
    return True if new_string == string else False

# AlgoExpert
# Time O(n^2) | Space O(n)
def isPalindrome6(string):
    new = ""
    for i in reversed(range(len(string))):
        new += string[i]
    return new == string

# Time O(n) | Space O(n)
def isPalindrome7(string):
    new = []
    for i in reversed(range(len(string))):
        new.append(string[i])
    return string == "".join(new)

# Time O(n) | Space O(n)
def isPalindrome8(string, i = 0):
    j = len(string) - 1 - i
    return True if i >= j else string[i] == string[j] and isPalindrome8(string, i + 1)

# Tail recursion
def isPalindrome9(string, i = 0):
    j = len(string) - 1 - i
    if i >= j:
        return True
    if string[i] != string[j]:
        return False
    return isPalindrome9(string, i + 1)

# Time O(N) | Space O(1)
def isPalindrome10(string):
    firstIdx = 0
    lastlIdx = len(string) - 1
    while firstIdx < lastlIdx:
        if string[firstIdx] != string[lastlIdx]:
            return False
        firstIdx += 1
        lastlIdx -= 1
    return True

string = 'abba'
print(isPalindrome1(string))
print(isPalindrome2(string))
print(isPalindrome3(string))
print(isPalindrome4(string))
print(isPalindrome5(string))
print(isPalindrome6(string))
print(isPalindrome7(string))
print(isPalindrome8(string))
print(isPalindrome9(string))
print(isPalindrome10(string))