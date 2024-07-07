'''
Soundex maps every name to a string consisting of one letter and three numbers, like M460.

One version of the algorithm is as follows:

Remove consecutive consonants with the same sound (for example, change ck -> c).
Keep the first letter. The remaining steps only apply to the rest of the string.
Remove all vowels, including y, w, and h.
Replace all consonants with the following digits:
b, f, p, v → 1
c, g, j, k, q, s, x, z → 2
d, t → 3
l → 4
m, n → 5
r → 6
If you don't have three numbers yet, append zeros until you do. Keep the first three numbers.
Using this scheme, Jackson and Jaxen both map to J250.

Implement Soundex.
'''

def soundex_orig(s):
    replacement = { 'bfpv': '1',
                    'cgjkqsxz': '2',
                    'dt': '3',
                    'l': '4',
                    'mn': '5',
                    'r': '6'
                    }
    deletions = "aoieuywh"

    s = s.lower().replace('ck', 'c')
    c0 = s[0].upper()

    s = s[1:]
    for c in deletions:
        print(c)
        s = s.replace(c, '')

    print(s)
    for rep, number in replacement.items():
        for c in rep:
            s = s.replace(c, number)

    print(s)
    res = [ c0, '0', '0', '0' ]
    l = max(len(s), 3)
    for i in range(l):
        res[i+1] = s[i]

    return ''.join(res)


import re

def soundex(name):
    name=re.sub(r'ck','c',name)
    name=re.sub(r'cs','c',name)
    first=name[0]
    name=name[1:]
    name=re.sub(r'[aoeuiywh]','',name)
    name=re.sub(r'[bfpv]','1',name)
    name=re.sub(r'[cgjkqsxz]','2',name)
    name=re.sub(r'[dt]','3',name)
    name=re.sub(r'l','4',name)
    name=re.sub(r'[mn]','5',name)
    name=re.sub(r'r','6',name)

    name=(first+name)[:4]
    return "{:0<4}".format(name)

s = 'Jackson'
print(soundex(s))


           