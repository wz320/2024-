n=int(input())
for i in range(n):
    distance=[]
    short=[]
    length,number=map(int,input().split())
    location=list(map(int,input().split()))
    location.sort()
    for i in location:
        distance2=length-i
        distance.append(distance2)
    for i in range(number):
       s=min(distance[i],location[i])
       short.append(s)
    s=max(short)
    l=max(location[-1],length-location[0])
    print(s,l)