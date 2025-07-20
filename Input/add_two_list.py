

def add_two_list(l1,l2):
    i=0
    b=0
    last=[]
    j=0
    while i< len(l1):
        a = l1[i]+l2[i]+j
        if (a>=10):
            a-=10            
            j=1  
        else:
            j=0

        i+=1
        last.append(a)

    return last

last_list= add_two_list([3,2,9,5],[4,6,5,3])
print(last_list)
for ind,num in enumerate(last_list):
    print("[{}]={}".format(ind,num))


## list , https://liaoxuefeng.com/books/python/basic/list-tuple/index.html