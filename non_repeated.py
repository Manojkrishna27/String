def nonrepeatedvalues(word):
    freq={}
    for ch in word:
        freq[ch]=freq.get(ch,0)+1 # hashing
    res=[]                  # empty list
    for ch in freq:
        if freq[ch]==1:
            res.append(ch)    # appending
    return res
word="Swiss"
print(nonrepeatedvalues(word))