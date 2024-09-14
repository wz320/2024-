cardlength=[]
b=2
while(True):
    a=eval(input())
    if a==0.00:
        break
    else:
        cardlength.append(a)
for i in range(len(cardlength)):
    while(True):
        if cardlength[i]>0:
            cardlength[i]=cardlength[i]-(1/b)
            b=b+1
        else:
            print(int(b-2), "card(s)")
            b=2
            break
