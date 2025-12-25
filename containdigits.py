def contain_digit(word):

    for ch in word:
        if ch >='0' and ch <='9': # ASCII range of character 
            return "String contain digits"   
        
        return "String not contain digits"

word="Manoj"
print(contain_digit(word)) 