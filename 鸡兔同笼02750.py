a=eval(input())
if a%2!=0:
    print("0 0")
elif a%4==0:
    print(int(a/4),int(a/2))
else:
    print(int(a/4)+1,int(a/2))
