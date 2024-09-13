from os.path import split
biaoge=input()
biaoge=biaoge.split()
n=eval(biaoge[0])
m=eval(biaoge[1])
a=eval(biaoge[2])
b=n//a+(n%a!=0)
c=m//a+(m%a!=0)
print(int(b*c))
