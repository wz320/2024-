n=int(input())
value=list(map(int,input().split()))
value.sort(reverse=True)
sum_=0
num=0
for i in value:
    if i+sum_>(sum(value)/2):
        num+=1
        break
    else:
        sum_+=i
        num+=1
print(num)