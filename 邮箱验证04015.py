def check1(address):
    return address.count('@')==1
def check2(address):
    return not(address[0] in '.@' or address[-1] in '.@')
def check3(address):
    weizhi=address.find('@')
    if address[weizhi-1]=='.' or address[weizhi+1]=='.':
        return False
    else:
        return '.' in address[weizhi:]
def check(address):
    return check1(address) and check2(address) and check3(address)
while True:
    try:
        address=input()
        if check(address)==1:
            print('YES')
        else:
            print('NO')
    except EOFError:
        break