
def lengthOfLongestSubString(s:str) ->int:
    n = len(s)
    ans =0  

    i,j = 0,0 
    lookup = set()
    while i<n and j<n: 
        if s[j] not in lookup:
            lookup.add(s[j])
            j+=1
            ans = max(ans,j-i)
        else:
            lookup.remove(s[i])
            i+=1
    return ans 

maxSubLen=lengthOfLongestSubString("abcabcbb")
print(maxSubLen)




