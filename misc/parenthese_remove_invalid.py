

def remove_invalid_parentheses_stack(s):
    # go through each char, 
    # if '(' then push index into stack
    # if ')', then 
    #    if stack not empty, pop
    #    if stack empty, the current ')' is invalid, remove it with s[index] =''
    #
    # after all chars finished, 
    # if still stack not empty, set s[all index in stack] to ''

    sl = list(s)
    stack = []
    for i, c in enumerate(sl):
        if c == '(':
            stack.append(i)
        elif c == ')':
            if not stack:
                sl[i] = ''
            else:
                stack.pop()
    
    for i in stack:
        sl[i] = ''
    
    return ''.join(sl)




def get_extra_parentheses(S):
    need_left, need_right = 0, 0
    for c in S:
        if c == '(':
            need_right += 1
        elif c == ')':
            need_right -= 1
            if need_right == -1:
                need_left += 1
                need_right = 0
    # extra left '(' = need_right
    # extra right ')' = need_left
    return need_right, need_left 

def is_valid_parentheses(S):
    extra_left, extra_right = get_extra_parentheses(S)
    return extra_left == 0 and extra_right == 0

def backtrack(S, i, extra_left, extra_right, res = set()):
    if i > len(S):
        return
    
    if i == len(S):
        if extra_left == 0 and extra_right == 0 and is_valid_parentheses(S):
            res.add(''.join(S))
        return
    
    if S[i] == '(' and extra_left > 0:
        S[i] = ''
        backtrack(S, i+1, extra_left - 1, extra_right, res)
        S[i] = '('
    elif S[i] == ')' and extra_right > 0:
        S[i] = ''
        backtrack(S, i+1, extra_left, extra_right - 1, res)
        S[i] = ')'
    
    # if it is (), run cases which keep it
    # if it is not (), directly check next index
    backtrack(S, i+1, extra_left, extra_right, res)

def get_valid_parentheses(s):
    res = set()
    extra_left, extra_right = get_extra_parentheses(s)
    backtrack(list(s), 0, extra_left, extra_right, res)
    return res

s='((a)())(000))))))'
print(get_valid_parentheses(s))

s='(()a(a)))(000))))))'
print(remove_invalid_parentheses_stack(s))



