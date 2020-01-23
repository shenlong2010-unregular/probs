'''
Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted string, the longest possible, containing distinct letters,

each taken only once - coming from s1 or s2.
'''

def longest1 (a1, a2):
    return "".join(sorted(set(a1 + a2)))

def longest2(s1, s2):
    # your code

    # Defining the Alphabet
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # Concatenating the Two Given Strings
    s = s1 + s2

    # Declaring the Output Variable
    y = ""

    # Comparing whether a letter is in the string
    for x in alphabet:
      if x not in s:
        continue
      if x in s:
        y = y + x

    # returning the final output
    return y

a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
print(longest1(a,b))
print(longest2(a,b))