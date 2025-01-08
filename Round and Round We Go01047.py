while 1:
    try:
        n=input()
        out=n
        num=int(n)
        lst=[num]
        ans=''
        for i in range(1,len(n)):
            n=n[1:]+n[0]
            lst.append(int(n))
        for i in range(1,len(lst)+1):
            if num*i not in lst:
                ans='not '
                break
        print(f'{out} is {ans}cyclic')
    except EOFError:
        break