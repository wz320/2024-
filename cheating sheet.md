```python
#方法一
while 1：
	try:
   
	except EOFError:
    	break
#方法二      
import sys
data=sys.stdin.read()
```

不知道输入多少的时候这么搞

```python
import random 
random_float = random.random()
print(random_float)
```

0-1的随机数

```python
import random
random_integer = random.randint(1, 10)
print(random_integer)
```

带范围的随机整数

```python
import random
random_float_range = random.uniform(1.0, 10.0)
print(random_float_range)
```

带范围的随机小数

```python
elements = ['apple', 'banana', 'cherry']
random_choice = random.choice(elements，n)
print(random_choice)
```

可以在一堆选择中随机选择n个

```python
from math import gcd #最大公约数
from math import lcm #最小公倍数
```

使用sqrt，ceil，floor，log之前不要忘了import math

log(真数，底数)

```python
import itertools
data=['a','b','c']
data2=['d','e']
print(list(itertools.permutations(data,2)))#从data中提取两个元素（不重复）排列的所有可能
[('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'c'), ('c', 'a'), ('c', 'b')]
print(list(itertools.combinations(data,2)))#从data中提取两个元素的所有可能
[('a', 'b'), ('a', 'c'), ('b', 'c')]
print(list(itertools.product(data,data2)))#分别从data和data2中提取一个元素进行排列组合
[('a', 'd'), ('a', 'e'), ('b', 'd'),('b','e'),('c','d')('c','e')]
print(list(itertools.product(data2,repeat=2)))#从两个data2表格中提取元素进行排列组合
[('d','d'),('d','e'),('e','d'),('e','e')]
```

排列组合的相关代码

```python
string.rstrip()
```

去掉字符串最后面的空格

```python
f'{number:.1f}'
```

将number变为一位小数

```python
pow(base,exp)
```

求base的exp次方

```python
n=int(input())
sub=[1]*n
lst=list(map(int,input().split()))
for i in range(n):
    for j in range(i):
        if lst[i]>lst[j]:
            sub[i]=max(sub[j]+1,sub[i])
print(max(sub))
```

dp求最长上升子序列的长度

```python
#基础的背包问题
n,b=map(int,input().split())
price=list(map(int,input().split()))
weight=list(map(int,input().split()))
item=[]
for i in range(n):
    item.append((price[i],weight[i]))
dp=[0]*(b+1)
for price,weight in item:
    for j in range(b,weight-1,-1):
        dp[j]=max(dp[j],dp[j-weight]+price)
print(dp[-1])
#完全背包问题
n,a,b,c=map(int,input().split())
dp=[0]+[-float('inf')]*n
for i in range(1,n+1):
    if i>=a:
        dp[i]=max(dp[i],dp[i-a]+1)
    if i>=b:
        dp[i]=max(dp[i],dp[i-b]+1)
    if i>=c:
        dp[i]=max(dp[i],dp[i-c]+1)
print(dp[n])
#变体（之前的会影响之后的）
n=int(input())
activity=[]
dp=[0]*63
for i in range(n):
    a,b=map(int,input().split())
    activity.append((a+1,b+1))
activity.sort()
for i in range(n):
    for j in range(activity[i][1],62):
        dp[j]=max(dp[j],dp[activity[i][0]-1]+1)
print(max(dp))
```

dp背包问题模版

```python
###经典dfs
def dfs(x, y):
    # 标记当前位置为已访问
    field[x][y] = '.'
    # 遍历8个方向
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        # 检查新位置是否在地图范围内且未被访问
        if 0 <= nx < n and 0 <= ny < m and field[nx][ny] == 'W':
            dfs(nx, ny)
n, m = map(int, input().split())
field = [list(input()) for _ in range(n)]
# 初始化8个方向
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
# 计数器
cnt = 0
# 遍历地图
for i in range(n):
    for j in range(m):
        if field[i][j] == 'W':
            dfs(i, j)
            cnt += 1

print(cnt)

###通过使用栈来模拟递归，可以避免因递归过深导致的栈溢出问题。
def dfs(x, y):
    stack = [(x, y)]
    while stack:
        x, y = stack.pop()
        if field[x][y] != 'W':
            continue
        field[x][y] = '.'  # 标记当前位置为已访问
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and field[nx][ny] == 'W':
                stack.append((nx, ny))
# 读取输入
n, m = map(int, input().split())
field = [list(input()) for _ in range(n)]
# 初始化8个方向
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
# 计数器
cnt = 0
# 遍历地图
for i in range(n):
    for j in range(m):
        if field[i][j] == 'W':
            dfs(i, j)
            cnt += 1
print(cnt)
```

dfs的两种模版

```python
#很好用的defaultdict，在输入一个之前没有的键的时候会返回一个默认值（空list，空set，int-0等）
from collections import defaultdict
#输出所有的key和value
list(a.items())
list(a.keys())
list(a.values())
```

关于字典的一些东西

```python
from collections import deque
def bfs(start, end):    
	q = deque([(0, start)])  # (step, start)
	in_queue = {start}
 	while q:
 		step, front = q.popleft() # 取出队⾸元素
		if front == end:
 		return step # 返回需要的结果，如：步⻓、路径等信息
# 将 front 的下⼀层结点中未曾⼊队的结点全部⼊队q，并加⼊集合in_queue设置为已⼊队
```

bfs模板

```python
maxn = 10;
sx = [-2,-1,1,2, 2, 1,-1,-2]
sy = [ 1, 2,2,1,-1,-2,-2,-1]

ans = 0;
 
def Dfs(dep: int, x: int, y: int):
    #是否已经全部走完
    if n*m == dep:
        global ans
        ans += 1
        return
    
    #对于每个可以走的点
    for r in range(8):
        s = x + sx[r]
        t = y + sy[r]
        if chess[s][t]==False and 0<=s<n and 0<=t<m :
            chess[s][t]=True
            Dfs(dep+1, s, t)
            chess[s][t] = False; #回溯
 

for _ in range(int(input())):
    n,m,x,y = map(int, input().split())
    chess = [[False]*maxn for _ in range(maxn)]  #False表示没有走过
    ans = 0
    chess[x][y] = True
    Dfs(1, x, y)
    print(ans)
```

递归回溯（马走日）

```python
from functools import cmp_to_key
```

如果排序超时了用这个

```python
#pylint:skip-file
```

如果报compile error试试这个

```python
import sys
sys.setrecursionlimit(30000)
```

设置递归深度

```python
d=[(0,1),(0,-1),(1,0),(-1,0)]
for i,(dx,dy) in enumerate(d):
    print(i,(dx,dy))
'''
输出：
0 (0,1)
1 (0,-1)
2 (1,0)
3 (-1,0)
'''
```

需要同时获取索引和内容的时候用

```python
from functools import lru_cache
```

这个可以使dfs变的更快且不爆栈
