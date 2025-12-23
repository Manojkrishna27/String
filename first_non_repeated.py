def firstnonrepeated(word):
    freq={}       # hashing method
    for ch in word:
        freq[ch]=freq.get(ch,0)+1 # getting ch into key value pair 
    
    for ch in freq:
        if freq[ch]==1:  # if ch == 1 the first ch will be return
            return ch    
    return -1
word="swiss"
print(firstnonrepeated(word))
