x=int(input())
while 1:
    if x==1:
        break
    else:
        if x%2==0:
            x=int(x/2)
            print('{}/2={}'.format(int(2*x),x))
        else:
            x=int(3*x+1)
            print('{}*3+1={}'.format(int((x-1)/3),x))