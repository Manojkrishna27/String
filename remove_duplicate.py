def remove_duplicate(word):
    seen=set() # set contain only unique element no duplicate
    res=[]   

    for ch in word:
        if ch not in seen:  # checking the character in seen
            seen.add(ch)     # if not add and append
            res.append(ch)

    return "".join(res) # converting list into string

    
word="bananas"
print(remove_duplicate(word))