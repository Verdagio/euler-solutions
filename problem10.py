
"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million."""

from math import sqrt

def solution10(target):

    return sum([x for x in sieves_prime(target)]) 

def sieves_prime(n):
    prime = [True for i in range(n+1)]
    p = 2
    while(p*p <= n):
        if(prime[p] == True):
            for i in range(p*2,n+1, p):
                prime[i] = False
        p += 1
    primeNums = []
    for p in range(2, n):
        if prime[p]:
            primeNums.append(p)
    return primeNums
    
print(solution10(2000000))
print(sieves_prime(100))