#CodeWar Challenge
def remove_vowels1(string):
    vowels = "aeiou"
    new_string = ''
    for vowel in string:
        if vowel not in vowels:
            new_string += vowel
    return new_string

# def remove_vowels(string):
#     vowels = "aeiou"
#     for vowel in vowels:
#         string = string.replace(vowel, "")
#     return string
# remove_vowels('hello')
# print(remove_vowels('ben'))
print(remove_vowels1('hello'))
# print(remove_vowels('apple'))