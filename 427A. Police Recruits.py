casenumber=int(input())
answer=0
person=0
case=list(map(int,input().split()))
for i in range(casenumber):
    if case[i]==-1 and person==0:
        answer=answer+1
    elif case[i]>0:
        person=person+case[i]
    elif case[i]==-1 and person>0:
        person=person-1
print(answer)
