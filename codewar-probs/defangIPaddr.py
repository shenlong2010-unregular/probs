# O(n) time, O(n)
def defangIPaddr(address):
    return address.replace('.', '[.]')

# O(N) space time
def defangIPaddr1(address):
    new_addr = ''
    for i in address:
        if i == '.':
            i = '[.]'
        new_addr += i
    return new_addr
print(defangIPaddr('255.100.50.0'))
print(defangIPaddr1('255.100.50.0'))