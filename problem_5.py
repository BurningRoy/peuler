# 2520 is the smallest number that can be divided by each
# of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all
# of the numbers from 1 to 20?

import time
def shrink_operand(num_list):
    back = - 1
    head = 0
    while num_list[back] != num_list[0]:
        while num_list[back] % num_list[head] == 0:
            num_list.remove(num_list[head])
        else:
            head += 1
            if num_list[head] == num_list[back]:
                back -= 1
                head = 0
    return num_list

def get_factors(num):
    factors = []
    divisor = 2
    while divisor < num:
        if num % divisor == 0:
            factors.append(divisor)
            for i in get_factors(num / divisor):
                factors.append(i)
            break
        else:
            divisor += 1
    else:
        factors.append(num)
    return factors
                

if __name__ == '__main__':
    start_time = time.time()
    nums = range(1,21)
    common_divisor = []
    shrink_operand(nums)
    for num in nums:
        l = get_factors(num)
        for each in l:
            if l.count(each) > common_divisor.count(each):
                common_divisor.extend([each] * (l.count(each) - common_divisor.count(each)))
            else:
                next

    multipand_result = 1
    for i in common_divisor:
        multipand_result *= i
    print multipand_result
    print "Time used: " + str(time.time() - start_time)
