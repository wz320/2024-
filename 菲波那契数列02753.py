import math
def Fibonacci(n):
    return int((1/math.sqrt(5))*(((1+math.sqrt(5))/2)**n-((1-math.sqrt(5))/2)**n))
n=int(input())
for i in range(n):
    print(Fibonacci(int(input())))
