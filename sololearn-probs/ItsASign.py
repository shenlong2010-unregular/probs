s = ['LIVE', 'LOVE', 'LAUGH', 'CHEESE']
# lst = [s.append(input().upper()) for _ in range(4)]
# print(s)
found = False
for item in s:
    
    if item[::-1] == item:
        print("Open")
        found = True
        break
    
if not found:
    print("Trash")
    