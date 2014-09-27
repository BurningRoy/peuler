# largest prime factor of 600851475143

# e.g
# The prime factors of 13195 are 5, 7, 13 and 29

import time

divisor = 2
dividend = 600851475143
start = time.time()

while divisor ** 2 < dividend:
    while dividend % divisor == 0:
        dividend = dividend / divisor
        #divisor = 2
    else:
        divisor += 1
else:
    print dividend

print time.time() - start
