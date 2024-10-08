import math
def prime(x):
    if x<2 or x%1!=0:
        return 'error'
    if x==2:
        return True
    for i in range(2,math.ceil(math.sqrt(x))+1):
        if x%i == 0:
            return False
    return True
ans=4
s=int(input())
lst=[x for x in range(1,s+1) if prime(x)==1]
for i in lst:
    if s-i in lst:
        ans=max(ans,i*(s-i))
print(ans)