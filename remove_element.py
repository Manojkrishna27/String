def removeelement(word,target):
    res=[]
    for ch in word:
        if ch!=target:
            res.append(ch) # append to the lis if != target

    return "".join(res) # then join the list into string

word="Hello world"
target="l"
print(removeelement(word,target))
