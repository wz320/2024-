k=int(input())
for i in range(k):
    n=int(input())
    sd=[]
    time_=1
    for j in range(n):
        s,d=map(int,input().split())
        sd1=[x for x in range(s,d+1)]
        sd.append(sd1)
    sd.sort()
    for l in range(len(sd)):
        sd[l]=set(sd[l])
    nowtime=sd[0]
    for m in range(len(sd)):
        if sd[m]&nowtime!=set():
            nowtime=nowtime&sd[m]
        else:
            nowtime=sd[m]
            time_+=1
    print(time_)