"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

import time

def is_prime(num, prim_list):
    #divisor = 2
    for item in prim_list:
        if num % item == 0:
            return False
    return True

if __name__ == '__main__':
    start_time = time.time()
    rounds = 10000
    start = 3
    primes = [2]
    while rounds > 0:
        if is_prime(start, primes):
            rounds -= 1
            primes.append(start)
        start += 2
    else:
        print "Final result: ", primes[-1]
    print time.time() - start_time
