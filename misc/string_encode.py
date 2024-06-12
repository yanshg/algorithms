'''
the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A"
'''

def encode(s: str) -> str:
    letter, num = '', 0
    res = ''
    for c in s:
        if c != letter:
            # encode
            if num > 0:
                res += str(num) + letter
            letter, num = c, 1
        else:
            num += 1
    
    if num > 0:
        res += str(num) + letter
        
    return res

s = 'AAAABBBCCDAA'
print(encode(s))