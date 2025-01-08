def josephus(people,number):
    queue=[x for x in range(1,int(people)+1)]
    while len(queue)>1:
        for i in range(int(number)-1):
            queue.append(queue.pop(0))
        queue.pop(0)
    return queue[0]
while True:
    n,m=map(int,input().split())
    if {n,m}=={0}:
        break
    print(josephus(n,m))