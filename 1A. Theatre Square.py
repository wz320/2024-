from os.path import split
biaoge=input()
biaoge=biaoge.split()
n=eval(biaoge[0])
m=eval(biaoge[1])
a=eval(biaoge[2])
if n%a==0:
    b=n//a
else:
    b=n//a+1
if m%a==0:
    c=m//a
else:
    c=m//a+1
print(int(b*c))
