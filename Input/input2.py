
'''
多行输入：
第一行为给定list的大小（比如：有n行数）
用n，m接受输入大小
用lis接受下面输入的矩阵
'''
n,m = map(int,input().strip().split())

print("n={},m={}".format(n,m))


lis=[]

for i in range(n):
    tmp=list(map(int,input().split()))
    print("i={},tmp={}".format(i,tmp))
    lis.append(tmp)


print(lis)


"""
hello
"""