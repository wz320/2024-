h=2*float(input())
m=int(input())
h-=m*0.5
classes=[]
add=0
for i in range(m):
    class1=tuple(map(float,input().split()))
    classes.append(class1)
classes.sort(key=lambda x:x[0]*x[-1],reverse=True)
for i in range(m):
    if h>=(5/classes[i][0]):
        h-=(5/classes[i][0])
        add+=5*classes[i][-1]
    else:
        add+=h*classes[i][0]*classes[i][-1]
        break
print(f'{add:.1f}')