import random
import math


# This is main function that is connected to the Test button. You don't need to touch it.
def prime_test(N, k):
    return fermat(N, k), miller_rabin(N, k)


# You will need to implement this function and change the return value.
def mod_exp(x, y, N):
    if y == 0:
        return 1
    z = mod_exp(x, math.floor(y / 2), N)
    if y % 2 == 0:
        return (z ** 2) % N
    else:
        return (x * (z ** 2)) % N


# You will need to implement this function and change the return value.
def fprobability(k):
    return 1 - 1 / (2 ** k)


# You will need to implement this function and change the return value.
def mprobability(k):
    return 1 - 1 / (4 ** k)


# You will need to implement this function and change the return value, which should be
# either 'prime' or 'composite'.
#
# To generate random values for a, you will most likley want to use
# random.randint(low,hi) which gives a random integer between low and
# hi, inclusive.
def fermat(N, k):
    if N > 2:
        for i in range(1, k + 1):
            if fermat_helper(N) == 'composite':
                return 'composite'
        return 'prime'
    else:
        return 'prime'


def fermat_helper(N):
    a = random.randint(1, N - 1)
    if mod_exp(a, N - 1, N) == 1:
        return 'prime'
    else:
        return 'composite'


# You will need to implement this function and change the return value, which should be
# either 'prime' or 'composite'.
#
# To generate random values for a, you will most likley want to use
# random.randint(low,hi) which gives a random integer between low and
#  hi, inclusive.
def miller_rabin(N, k):
    if N > 2:
        for i in range(1, k + 1):
            if miller_rabin_helper(N) == 'composite':
                return 'composite'
        return 'prime'
    else:
        return 'prime'


def miller_rabin_helper(N):
    a = random.randint(1, N - 1)
    exp = N - 1
    if exp % 2 != 0:
        return 'composite'
    while exp % 2 == 0:
        z = mod_exp(a, exp, N)
        if z == N - 1:
            return 'prime'
        elif z != 1:
            return 'composite'
        exp = exp / 2
    return 'prime'
