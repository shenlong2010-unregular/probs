# O(N) ST
def caesarCipherEncryptor(string, key):
    result = ""
    newkey = key % 26
    for i in string:
        if i.islower():
            result += chr((ord(i) + key - 97) % 26 + 97)
        elif i.upper():
            result += chr((ord(i) + key - 65) % 26 + 65)
    return result
print(caesarCipherEncryptor('xyz', 2))
print(caesarCipherEncryptor('XYZ', 2))
print(caesarCipherEncryptor('Xyz', 2))
