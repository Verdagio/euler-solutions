# Smallest multiple
# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all
#  of the numbers from 1 to 20?


def solution5(max):

    l = [x for x in range(2, max + 1)]
    i = 1
    while True:
        if helper(l, i):
            return i
        else:
            i = i + 1


def helper(ls, i):
    if len(ls) <= 0:
        return True
    else:
        if i % ls[0] != 0:
            return False
        if i % ls[0] == 0:
            return helper(ls[1:], i)
        else:
            return False


print(solution5(10))
# print(solution5(20))
