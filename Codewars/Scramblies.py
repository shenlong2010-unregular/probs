from collections import Counter

#Space O(n) | Time O(n)
def scramble(s1, s2):
    cnt = Counter(s1)
    # print(cnt)
    cnt.subtract(Counter(s2))
    # print(cnt)
    # print(cnt.values())
    return (all(e >= 0 for e in cnt.values()))
    
print(scramble('rkqodlw','world'),True)
# print(scramble('cedewaraaossoqqyt','codewars'),True)
print(scramble('katas','steak'),False)
# print(scramble('scriptjava','javascript'),True)
# print(scramble('scriptingjava','javascript'),True)
print(scramble('javscripts','javascript'),True)

def scramble(s1,s2):
    for c in set(s2):
        if s1.count(c) < s2.count(c):
            return False
    return True