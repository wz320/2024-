def trans2(a):
    ans=bin(a)
    ans=ans.replace('0b','')
    return ans
x=trans2(int(input()))
if x[::-1]==x:
    print('Yes')
else:
    print('No')