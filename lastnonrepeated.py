def lastnonrepeated(word):
    freq={}
      # Step 1:frequency count
    for ch in word:
        freq[ch]=freq.get(ch,0)+1
    # Step 2:traverse from right to left
    for ch in range(len(word)-1,0,-1):
        if freq[word[ch]]==1:
            return word[ch]
    return -1
        
word="Swiss"
print(lastnonrepeated(word))