while True:
    N=int(input())
    if N==0:
        break
    total=[]
    candidate=1
    for i in range(N):
        hotel=tuple(map(int,input().split()))
        total.append(hotel)
        total.sort()
    least=total[0]
    for j in total[1:]:
        if j[-1]<least[-1]:
            candidate+=1
            least=j
    print(candidate)