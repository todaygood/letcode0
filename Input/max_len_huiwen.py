def is_huiwen(s:str):
    i,j=0,len(s)-1

    while i<j:
        if s[i] == s[j]:
            i+=1
            j-=1
        else:
            return False
    
    return True
           
#print(is_huiwen("bacab"))

def find_max_length_huiwen(s: str):

    n = len(s)
    max_len =0 
    start =0 

    for i in range(n):
        for j in range(i,n):
            if is_huiwen (s[i:j+1]) and (j-i+1)> max_len:
                max_len = j-i+1 
                start =i 
    
    return s[start:start+max_len]
    

        
    


huiwen_str= find_max_length_huiwen("babad")

print(huiwen_str)



## https://cloud.tencent.com/developer/article/2450047

## https://www.bilibili.com/video/BV1w7421Z798/?spm_id_from=333.337.search-card.all.click&vd_source=32c774556175602ebc0443b3c0331c05