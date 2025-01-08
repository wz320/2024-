def Pell(x):
    plustime=2
    a=1
    b=2
    if x==1:
        return 1
    if x==2:
        return 2
    else:
        lst=[1,2]+[0]*(x-2)
        for i in range(2,x):
            lst[i]=(2*lst[i-1]+lst[i-2])%32767
        return int(lst[-1])
n=int(input())
for i in range(n):
    print(Pell(int(input())))