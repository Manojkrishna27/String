name="programming"
freq={}
for ch in name:
    freq[ch]=freq.get(ch,0)+1 # getting key and value

for ch in freq:
    if freq[ch]>1: # checking value greater than 1
        print(ch,freq[ch])