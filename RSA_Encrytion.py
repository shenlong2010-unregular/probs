# RSA Crypto system
# Example:
# A -> 1
# B -> 2
# C -> 3
# D -> 4
# convert text to number

# cryptography symmetry
def encyption(num1, num2): #num1, num2 is the lock number
    letter = 'B'
    # we have letter B, we have number of character along with it is 2 as example
    number = 2
    result = (number ** num1) % num2 # this result is ciphertext
    return result
print(encyption(5, 14)) # result in letter D as ciphertext

# ciphertext is not an original character, but it's based on origin character

# decryption would need the result from encryption
def decryption(num1, num2, ciphertext):
    result = (ciphertext ** num1) % num2
    return result
print(decryption(11, 14, encyption(5,14)))
