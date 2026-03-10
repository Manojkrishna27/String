word="timisaplayertimplayscrickettimisatim"   
check="tim"
count=0
for i in range(len(word)-len(check)+1):
    if word[i:i+3]==check:
        count+=1
print(count)
    