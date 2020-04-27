from collections import Counter
# O(n) SP
def anagrams(word, words):
    lst = []
    s1 = Counter(word)
    # print(s1)
    for i in words:
        # print(i)
        compare = Counter(i)
        # print(compare)
        if s1 == compare:
            lst.append(i)
        
    return lst

print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))

def anagrams(word, words): 
    return [item for item in words if sorted(item)==sorted(word)]