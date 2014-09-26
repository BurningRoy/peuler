# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

numbers = set(range(0, 1000, 3)).union(set(range(0, 1000, 5)))
result = 0
for i in numbers:
    result += i
print result