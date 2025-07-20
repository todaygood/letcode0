
def twoSum(nums,target):
    i,j=0,1
    tl = len(nums)
    while i < tl-1:  
        j=i+1      
        while j<tl:
            if nums[i]+nums[j] == target:
                return i,j
            j+=1
        i+=1
    


i,j= twoSum([1,2,3,5,7],12)
print("i={},j={}".format(i,j))

