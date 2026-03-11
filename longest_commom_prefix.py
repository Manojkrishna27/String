def longest_common_prefix(arr):

    arr.sort()

    first=arr[0] # take first
    last=arr[-1] # and take last 
    
    i=0
    while i<len(first) and i<len(last) and first[i]==last[i]: # use this logic 
        i+=1    # if satisfy 
    return first[:i]    # return first slice
arr=["fly","flowers","flag","flew"]
print(longest_common_prefix(arr))