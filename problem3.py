from math import floor, sqrt, ceil
# Largest prime factor
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def prime_factors(number):
    result = []
    if number == 2:
        result.append(2)
        return result
    for i in range(3, floor(sqrt(number))):
        if number % i == 0:
            if len(prime_factors(i)) == 0:
                result.append(i)
    return result


print("Problem 3 answer: ", prime_factors(600851475143)[-1])
