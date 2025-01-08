a=input().lower()
b=1
c=[]
for i in range(1,len(a)):
    if a[i]!=a[i-1]:
        c.append('('+a[i-1]+','+str(b)+')')
        b=1
    else:
        b+=1
c.append('('+a[-1]+','+str(b)+')')
print(''.join(c))


