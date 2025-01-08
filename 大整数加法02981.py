def del0(x):
    i=0
    while x[i]==0:
        del x[i]
        i+=1
    return x
a=int(del0(input()))
b=int(del0(input()))
print(a+b)