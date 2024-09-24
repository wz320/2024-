a=input().split()
L=eval(a[0])
M=eval(a[1])
tree=[x for x in range(L+1)]
for i in range(M):
    b=input().split()
    begin=eval(b[0])
    finish=eval(b[1])
    tree=[x for x in tree if x<begin or x>finish]
print(len(tree))