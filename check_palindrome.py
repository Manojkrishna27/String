"""Palindrome is a string which gives same word when we reverse it"""
# two pointer method
def palindrome(word):
    rev=list(word)
    i=0  
    j=len(word)-1
    while i<j:
        if rev[i]!=rev[j]:  # checking if first word not equal to last word 
            return False # palindrome
        i+=1
        j-=1
    return True # palindrome
word="madam"
print(palindrome(word))