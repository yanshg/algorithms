'''
Given a string containing parenthesis (), braces {}, brackets [], and angle brackets <>, write a
function to return True if that string is balanced, and False otherwise.


A string is considered balanced if each opening bracket is followed by a matching closing bracket
at the same nesting level, and each closing bracket has been preceded by a matching opening bracket
also at the same nesting level.


Some examples:


"some string" => True


"[abc(def)gh{i}j]" => True


"[abcdef" => False (no closing bracket)


"abcd(egf))" => False (extra closing parenthesis)


")abcd((egf)" => False (extra closing parenthesis at the start)


"(abcd[)]efgh" => False (closing parenthesis is not nested at the same level as the opening one)

'''

def check_if_balanced_brackets(s):

    pairs = { ')': '(', '}': '{', ']': '[', '>': '<' }
    stack = []
    for c in s:
        if c in "({[<":
            stack.append(c)
        elif c in ")}]>":
            if not stack or stack[-1] != pairs[c]:
                return False
            stack.pop()
    return len(stack) == 0

s = "some string"
assert check_if_balanced_brackets(s)

s = "[abc(def)gh{i}j]"
assert check_if_balanced_brackets(s)

s = "abcd(egf))"
assert not check_if_balanced_brackets(s)

s = ")abcd((egf)"
assert not check_if_balanced_brackets(s)

s = "(abcd[)]efgh"
assert not check_if_balanced_brackets(s)
