import time
start = time.time()
number = 600851475143
divisor = 2

while divisor ** 2 < number:
    while number % divisor == 0:
        number /= divisor
    divisor += 1

print(number)
print time.time() - start
