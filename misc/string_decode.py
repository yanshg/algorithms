'''
given a string encoding: a1b2c2 (lower case alphabets followed with their count)= abbcc

'''

def decode(s):
    letter, num = '', 0
    res = ''

    for c in s:
        if c.isdigit():
            num += num * 10 + int(c)
        else:
            if num > 0:
                # normal case
                res += num * letter
            elif num == 0 and letter != '':
                # not start position and only letter (no number)
                res += c
            num = 0
            letter = c

    if num > 0 and letter != '':
        # remaining normal case
        res += num * letter
    elif num == 0 and letter != '':
        # remaining letter
        res += letter

    return res

assert decode('a1b2c2') == 'abbcc'

print(decode('a'))
print(decode('11'))
print(decode('11a'))
print(decode('a2bb2c'))
