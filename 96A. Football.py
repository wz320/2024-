situation=input()
a=0
for i in range(len(situation)-6):
    if situation[i:i+7]=='0000000' or situation[i:i+7]=='1111111':
        a+=1
if a!=0:
    print('YES')
else:
    print('NO')