a=int(input())
i=6
while i<=a:
    if a%i!=0:
        i+=1
    else:
        print(a//i)
        break