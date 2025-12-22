def reverseword(word):
    # two pointer
    i=0 # start
    j=len(word)-1 # end
    rev=list(word)  # expliciting the string to list because string is immutable 
    while i<j:
        rev[i],rev[j]=rev[j],rev[i] #swap
        i+=1   # forward
        j-=1    #backward
    return "".join(rev)  
word="hello word"
print(reverseword(word))