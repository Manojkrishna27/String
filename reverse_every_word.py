def reverse_every_word(word):
    rev=word.split() # spliting into each word
    print(rev) # check how it is splitted for learning
    rev.reverse() # reverse each
    return " ".join(rev)  # and join with space
word="Hi i am Manoj"
print(reverse_every_word(word))