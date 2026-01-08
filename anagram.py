def is_anagram(s1, s2):
    # anagram is all about the length of two string is same  character  and count 
    # checking length
    if len(s1) != len(s2):
        return False

    count = {} # empty dict

    for ch in s1:
        count[ch] = count.get(ch, 0) + 1 # hashing method 

    for ch in s2:
        if ch not in count:
            return False
        count[ch] -= 1
        if count[ch] < 0:
            return False

    return True

print(is_anagram("race", "care"))   # True
print(is_anagram("aab", "abb"))     # False
