s=''
total_l=0
lst=[0]
for i in range(1,31500):
    s+=str(i)
    l_k=len(s)
    total_l+=len(s)
    lst.append(total_l)
t=int(input())
for i in range(t):
    n=int(input())
    for j in range(len(lst)):
        if lst[j]>=n:
            ans=j
            break
    location=n-lst[ans-1]-1
    print(s[location])