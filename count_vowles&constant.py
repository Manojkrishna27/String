def count_vowels_consonants(word):
    word=word.lower() # this will convert A to a capital to lower
    vowels=0
    consonants=0
    for ch in word:
        if ch in "aeiou":  # checking ch in vowels
            vowels+=1
        elif ch.isalpha(): # this ensure that we will only count the actual letters
            consonants+=1
    return "the vowels in a string:",vowels,"the consonants in a String:", consonants
word="apple1"
print(count_vowels_consonants(word))