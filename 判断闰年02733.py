a=eval(input())
if a%100==0 and a%400!=0 or a%4!=0:
    print("N")
else:
    print("Y")