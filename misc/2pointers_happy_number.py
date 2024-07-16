'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

1 ^ 2 + 9^2 = 82

8 ^ 2 + 2 ^ 2 = 68

6 ^ 2 + 8 ^ 2 = 100

1 ^ 2 + 0 ^ 2 + 0 ^ 2 = 1
'''

def get_next_number(num):
    next_num = 0
    while num:
        last_digit = num % 10
        next_num += last_digit * last_digit
        num //= 10
    return next_num

def is_happy_number(num):
    # base case
    if not num:
        return False
    
    # check if loop endlessly
    slow, fast = num, num
    while fast and fast != 1:
        slow = get_next_number(slow)
        fast = get_next_number(get_next_number(fast))
        if slow == fast:
            # loop endlessly
            break
    
    return fast == 1

print(is_happy_number(19))


