def security(s):
    parts = s.partition('$')
    # print(parts[0])
    # print(parts[1])
    # print(parts[2])
    if len(parts[0]) == 1 and 'T' in parts[0] or len(parts[2]) == 1 and 'T' in parts[2]:
        return 'ALARM'
    if 'T' in parts[0][s.find('G'):-1] or 'T' in parts[2][:s.find('G')+1]:
        return 'ALARM'
    else:
        return 'quiet'

print(security('T$xxxxxxG'), 'ALARM')
print(security('xxxGGxx$xxGxxT'), 'quiet')
print(security('xxxxxGxx$xxxT'), 'ALARM')


# if 'T' in (s[(s.find('G')):(s.find('$')+1)]) or 'T' in (s[s.find('$'):s.find('G', s.find('$'))+1]):
#     print('ALARM')
# else:
#     print('quiet')

# print('ALARM' if 'T' in s[s.find('G'):s.find('$')+1] else 'quiet')
# print(True if 'T' in s[s.find('$'):s.find('G', s.find('$'))+1] else False)