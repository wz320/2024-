import math
n=int(input())
for i in range(n):
    x=int(input())
    ans=(1+x)*x/2-2*(2**math.ceil(math.log(x,2))-1)
    print(int(ans))