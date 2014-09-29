# A palindromic number reads the same both ways.
# The largest palindrome made from the product of
# two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
import time

def is_palindrome(number):
    """ Determine whether a number is palindrome """
    n_str = str(number)
    length = len(n_str)
    #middle = int(round(len(n_str)/2.0))
    #return n_str[0:middle:1] == n_str[-1:-(middle + 1):-1]
    for i in range(length):
        if n_str[i] == n_str[length - i - 1]:
            continue
        else:
            return False
    return True
        
def get_multiplier_multiplicant(number):
    """ Reture multiplier and multiplicant """
    multiplier = 999
    while multiplier >= 100:
        remainder = number % multiplier
        if remainder == 0:
            multiplicand = number / multiplier
            if multiplicand >= 100 and multiplicand <= 999:
                return (multiplier, multiplicand)
            else:
                multiplier -= 1
        else:
            multiplier -= 1
    else:
        return False
    
if __name__ == '__main__':

    start_time = time.time()
    start = 1000 ** 2
    end = 100 ** 2
    while start >= end:
        if not is_palindrome(start):
            start -= 1
        else:
            result = get_multiplier_multiplicant(start)
            if not result:
                start -= 1
            else:
                print result, start
                break
    print time.time() - start_time
