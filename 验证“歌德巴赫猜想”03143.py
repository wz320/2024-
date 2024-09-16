def prime(n):
    if n<=1 or n%1!=0:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
ylist=[]
zlist=[]
x=int(input())
if x<6 or x%2!=0:
    print("Error!")
else:
    sushu=[a for a in range(int(x/2)+1) if prime(a)==1]
    for j in sushu:
        y=x-j
        if prime(y)==1:
            ylist.append(j)
            zlist.append(y)
        else:
            y=0
for k in range(len(ylist)):
    print(x,"=",ylist[k],"+",zlist[k],sep="")