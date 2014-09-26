# largest prime factor of 600851475143

# e.g
# The prime factors of 13195 are 5, 7, 13 and 29

divisor = 2
dividend = 600851475143

while divisor < dividend:
    remainder = dividend % divisor
    if remainder == 0:
        dividend = dividend / divisor
        divisor = 2
    else:
        divisor += 1
else:
    print divisor

