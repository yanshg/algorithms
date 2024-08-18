'''
i18n match internationalization

f6k match facebook

f2eb2k match facebook

8 match facebook

'''

def match(s, p):
    num = 0

    ls, lp = len(s), len(p)
    i, j = 0, 0
    while i < ls and j < lp:
        # Handle the current letter or number for both s and p
        cs, cp = s[i], p[j]
        if cp.isdigit():
            num = int(cp)
            while j+1 < lp and p[j+1].isdigit():
                num = num * 10 + int(p[j+1])  
                j += 1              
            i += num - 1
        elif cs != cp:
            return False

        # Get to next section                         
        i += 1
        j += 1

    return i == ls and j == lp

assert match('facebook', 'f6k')
assert not match('facebook', 'f6')