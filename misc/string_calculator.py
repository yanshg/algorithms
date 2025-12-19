
from collections import deque

# consider +- as sign
# use one stack to store number results
# use deque to pop left with O(1)
# use recursion for "(expression)"
def calculator(s):
    if not s:
        return 0
    
    def helper(slist):
        sign = '+'
        num = 0

        stack = []

        while len(slist) > 0:
            c = slist.popleft()
            if c.isdigit():
                num = num * 10 + int(c)
            if c == '(':
                num = helper(slist)
            if c in "+-*/)" or len(slist) == 0:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack[-1] *= num
                elif sign == '/' and num != 0:
                    stack[-1] //= num
                sign = c
                num = 0
            if c == ')':
                break
        return sum(stack)

    return helper(deque(list(s.replace(' ', ''))))

# consider +-*/ as operator
# use 2 stacks, one for numbers, one for operators
# use iteration to support "(expression)"

# cases:  1 + 2 * 3
#         1 * 2 + 3

# Notes:  the sequence is reversed after pop()
def calculate(operator, num1, num2):
    # num1 is second 
    # num2 is first
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num2 - num1
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num2 // num1

# check if op2 has higher precedence than op1
def has_precedence(op1, op2):
    if op2 in '*/':
        return True
    return False

def calculator1(s):
    if not s:
        return 0
    
    def helper(slist):
        # add 0 as first item to support case like "-7 + 1"
        nums = [0]
        operators = []

        i = 0
        n = len(slist)
        while i < n:
            c = slist[i]
            if c.isdigit():
                num = int(c)
                while i+1 < n and slist[i+1].isdigit():
                    num = num * 10 + int(slist[i+1])
                    i += 1
                nums.append(num)
            elif c == '(':
               operators.append(c)
            elif c in "+-*/":
                # calculate the precedent operator
                if operators and has_precedence(c, operators[-1]) and len(nums) >= 2:
                    nums.append(calculate(operators.pop(), nums.pop(), nums.pop()))
                operators.append(c)
            elif c == ')':
                # calculate the operators until get to '('
                while operators and operators[-1] != '(' and len(nums) >= 2:
                    nums.append(calculate(operators.pop(), nums.pop(), nums.pop()))
                # pop last operator '('
                operators.pop()
            i += 1

        # calculate the remaining operators
        while operators and len(nums) >= 2:
            nums.append(calculate(operators.pop(), nums.pop(), nums.pop()))

        return nums[-1] if nums else 0  

    return helper(list(s.replace(' ', '')))


s = '-7 * (8+8)  /4'
print(calculator(s))

s = "(2+6* 3+5- (3*14/7+2)*5)+3"
print(calculator(s))

s = '-7 * (8+8)  /4'
print(calculator1(s))

s = "(2+6* 3+5- (3*14/7+2)*5)+3"
print(calculator1(s))
