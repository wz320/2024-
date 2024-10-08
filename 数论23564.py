import math

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def prime_factors(n):
    factors = []
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            factors.append(i)
    return factors

def has_square_factor(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % (i * i) == 0:
            return True
    return False

def miu(n):
    if has_square_factor(n):
        return 0
    primes = prime_factors(n)
    if len(primes) % 2 == 0:
        return 1
    else:
        return -1

x = int(input())
print(miu(x))