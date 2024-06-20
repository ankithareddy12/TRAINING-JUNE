#3 combinations
"""def combinations(lst):
    n=len(lst)
    comb=[]
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                comb.append([lst[i],lst[j],lst[k]])
    return comb

l=[3,2,5,4,1,6,8]
r=combinations(l)
print(r)

def gen_comb(arr,n):
    def combin(comb,start):
        if len(comb)==n:
            print(comb)
            return
        for i in range(start,len(arr)):
            comb.append(arr[i])
            combin(comb,i+1)
            comb.pop()
    combin([], 0)
#arr=list(map(int,input().split()))
arr=[3,2,5,4,1,6,8]
print(gen_comb(arr,3))


def gen_comb(arr,n):
    def combin(comb,start):
        if len(comb)==n:
            print(comb)
            return
        for i in range(start,len(arr)):
            comb.append(arr[i])
            combin(comb,i+1)
            comb.pop()
    combin([], 0)
arr=list(map(int,input().split()))
print(gen_comb(arr,3))"""


