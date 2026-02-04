name="programming"
freq={}
for ch in name:
    freq[ch]=freq.get(ch,0)+1

for ch in freq:
    if freq[ch]>1:
        print(ch,freq[ch])