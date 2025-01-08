n=int(input())
origin=[x for x in range(1,n+1)]
origin=set(origin)
person=sorted(list(map(int,input().split())))
now=set(person)
for i in range(len(person)):
    if person[i]==person[i-1]:
        person[i]+=0.5
now1=set(person)
correct=now&origin
lost=sorted(origin-correct)
add=list(sorted(now1-correct))
for i in range(len(add)):
    add[i]=int(add[i]//1)
print(' '.join(map(str,lost)))
print(' '.join(map(str,add)))