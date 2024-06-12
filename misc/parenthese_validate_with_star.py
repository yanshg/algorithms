'''
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis'('must have a corresponding right parenthesis')'.

Any right parenthesis')'must have a corresponding left parenthesis'('.

Left parenthesis'('must go before the corresponding right parenthesis')'.

'*'could be treated as a single right parenthesis')'or a single left parenthesis'('or an empty string.

An empty string is also valid.

'''


# Solution with O(3^m): m is number of '*' in string

# ((*)(()*)

def is_valid_parenthese(s):
    need = 0
    for c in s:
        if c == '(':
            need += 1
        elif c == ')':
            need -= 1
            if need < 0:
                return False
    return need == 0

def backtrack(s, i, res):
    if i == len(s):
        if is_valid_parenthese(s):
            res.add(''.join(s))
        return
        
    if s[i] == '*':
        for c in "( )":
            s[i] = c
            backtrack(s, i+1, res)
            s[i] = ''
    else:
        backtrack(s, i+1, res)
        
    return

def check_wild_parenthese(s):
    res = set()
    backtrack(list(s), 0, res)
    return res


# O(n) solution

'''
思路: 用两个变量，
low表示把"*"看做右括号时，左括号的个数(即左括号的lower bound), 
high表示把"*"看做左括号时，左括号的个数(即左括号的upper bound)。

显然，当high小于0时，说明即使把"*"看做左括号, 也不能够抵消右括号，所以返回false。

那么从左到右扫一遍输入string，遇到左括号时，low和high都加1，
遇到右括号时，只有low大于0时才减1,这是为了保证low不小于0，high减1。
遇到"*"时，根据high的定义high加1，low大于0才减1。

最后查看low的个数即可。


同时检查，  
    1. 所有 * 为 '(' 时， if need_right get to negative, which means extra ) exists
    2. 所有 * 为 ')' 时， if need_right get to negative, which means extra ( exists


'''

def check_valid_parenthesis_string(s):
    low, high = 0, 0

    for c in s:
        if c == '(':
            low += 1
            high += 1
        elif c == ')':
            if low > 0:
                low -= 1
            high -= 1
        else:
            if low > 0:
                low -= 1
            high += 1

        if high < 0:
            return False
    return low == 0
    
print(check_valid_parenthesis_string("**(((("))


# O(n) solution
#
# Two failure cases:
#
# 1. change all '*' to '(', check if any extra ')' exists, like: (***))))))
# 2. change all '*' to ')', check if any extra '(' exists. like: (((((***)
#
# If no extra ')' and no extra '(', then it is valid parenthese string

def check_if_extra_right_parenthese(s):
    need_right = 0
    for c in s:
        # assume '*' is '('
        if c == '(' or c == '*':
            need_right += 1
        elif c == ')':
            need_right -= 1
            if need_right < 0:
                return True
    return False

def check_if_extra_left_parenthese(s):
    need_left = 0
    for c in reversed(s):
        # assume '*' is ')'
        if c == ')' or c == '*':
            need_left += 1
        elif c == '(':
            need_left -= 1
            if need_left < 0:
                return True
    return False

def is_valid_parenthesis_string_simple(s):
    if check_if_extra_left_parenthese(s) or check_if_extra_right_parenthese(s):
        return False
    return True

assert not is_valid_parenthesis_string_simple(")")
assert is_valid_parenthesis_string_simple("(()*()")
assert not is_valid_parenthesis_string_simple("***(((")
assert is_valid_parenthesis_string_simple("((***")

s = "'(()*'"
print(is_valid_parenthesis_string_simple(s))

s = "'***(((((()*'"
print(is_valid_parenthesis_string_simple(s))