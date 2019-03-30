# 10001st Prime
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
# we can see that the 6th prime is 13.
# What is the 10 001st prime number?

def solution7(target=10001):
    count = 0
    i = 0
    while count <= target:
        if i > 1 and i < 4:
            
            count+=1
        elif i > 3:
            if isprime(i):
                
                count+=1
                if count == target:
                    return i
        i+=1

# brute force method of checking if a number is prime
def isprime(num):
    if any([num % i == 0 for i in range(2,num) if i != num]):  
        return False
    return True

print(solution7())