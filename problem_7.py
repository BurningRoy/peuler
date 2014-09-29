"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
# Brute force solution

import time

def is_prime(num):
    divisor = 2
    while divisor < num:
        if num % divisor == 0:
            return False
        else:
            divisor += 1
    else:
        return True

if __name__ == '__main__':
    start_time = time.time()
    rounds = 10000
    start = 3
    while rounds > 0:
        if is_prime(start):
            #start += 1
            #print "Got: ", rounds, "Number: ", start
            rounds -= 1
        start += 2
        #time.sleep(1)
    else:
        print "Final result: ", start - 2
    print time.time() - start_time
        
