n=int(input())
sentence=input().split()
row=''
answer=[]
row+=sentence[0]
for i in range(1,n):
    if len(row)+len(sentence[i])<80:
        row=row+' '+sentence[i]
    else:
        answer.append(row.rstrip())
        row=sentence[i]
answer.append(row.rstrip())
print('\n'.join(answer))

