"""
Involves evaluating a mathematical expression given as a string. 

The expression includes non-negative integers and the operators +, -, *, and /. 
The goal is to compute the result of the expression following the standard operator precedence rules, where multiplication and division are performed before addition and subtraction.

"""

class Solution:
    def calculate(self, s: str) -> int:
        l = len(s)
        stack = []
        num = 0
        sign = '+'
        
        for i, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)
            if c in "+-*/" or i == l-1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    stack.append(int(stack.pop() / num))
                sign = c
                num = 0
        
        return sum(stack)

# Example usage:
solution = Solution()
result = solution.calculate("3+2*2")
print(result)  # Output: 7
