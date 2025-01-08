n=int(input())
shiti=0
for i in range(n):
    sentence=list(map(str,input().split()))
    if '###' in sentence[0]:
        shiti+=1
    for j in range(1,len(sentence)):
        if '###' in sentence[j] and '###' not in sentence[j-1]:
            shiti+=1
print(shiti)