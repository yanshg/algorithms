"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

"""

def backspace_compare(s,t):
    def build(s):
        skip=0
        for x in reversed(s):
            if x=='#':
                skip += 1
            elif skip > 0:
                skip -= 1
            else:
                yield x

    return list(build(s)) == list(build(t))

assert backspace_compare("","")
assert backspace_compare("a#c","b#c")
assert backspace_compare("a#c#","b#c#")
assert backspace_compare("a##c#","b#c#")
assert not backspace_compare("aa#c#","bb#c#")
assert not backspace_compare("a","bb")
