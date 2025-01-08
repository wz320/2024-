n=int(input())
answer=[]
xishu=[]
for i in range(n):
    xishu=xishu+input().split()
    a=eval(xishu[0+3*i])
    b=eval(xishu[1+3*i])
    c=eval(xishu[2+3*i])
    if a>0:
        x1=(-b+(b**2-4*a*c)**0.5)/(2*a)
        x2=(-b-(b**2-4*a*c)**0.5)/(2*a)
    else:
        x1=(-b-(b**2-4*a*c)**0.5)/(2*a)
        x2=(-b+(b**2-4*a*c)**0.5)/(2*a)
    if b*b-a*4*c>=0:
        x1=f"{round(x1,5):.5f}"
        x2=f"{round(x2,5):.5f}"
    else:
        x1=f"{round(x1.real,5):.5f}"+"+"+f"{round(x1.imag,5):.5f}"+"i"
        x2=f"{round(x2.real,5):.5f}"+f"{round(x2.imag,5):.5f}"+"i"
    answer.append(x1)
    answer.append(x2)
for i in range(n):
    x1=answer[0+2*i]
    x2=answer[1+2*i]
    if x1==x2:
        print("x1=x2=",x1,sep="")
    else:
        print("x1=",x1,";","x2=",x2,sep="")