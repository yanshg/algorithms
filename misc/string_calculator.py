def calculator(s):
    
    def helper(slist):
        sign = '+'
        num = 0

        stack = []

        while len(slist) > 0:
            c = slist.pop(0)
            if c.isdigit():
                num += num * 10 + int(c)
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

    slist = list(s.replace(' ', ''))
    return helper(slist)

s = '-7 * (8+8)  /4'
print(calculator(s))

s = "(2+6* 3+5- (3*14/7+2)*5)+3"
print(calculator(s))