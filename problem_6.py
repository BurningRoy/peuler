"""
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""

# expand (a + b + c)(a + b + c) = a * a + b * b + c * c + 2ab + 2ac + 2bc
# Hence the difference should be: 2ab + 2ac + 2bc
import time

def sum_square_difference(ops_list): # ops_list is a list of operands
    result = 0
    while len(ops_list) > 1:
        first_operand = ops_list[0]
        ops_list = ops_list[1::1]
        for i in ops_list:
            result = result + first_operand * i
    return result * 2


if __name__ == '__main__':
    start_time = time.time()
    ops_list = range(1, 101, 1)
    print "Result: ", sum_square_difference(ops_list)
    print "Time used: ", time.time() - start_time
