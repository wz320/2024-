number=int(input())
qiuhe=0
a=1
while(a<=number):
    if "7" not in str(a) and a%7!=0:
        qiuhe=qiuhe+a*a
    else:
        qiuhe=qiuhe+0
    a=a+1
print(qiuhe)
