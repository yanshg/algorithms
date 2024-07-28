# We can compare two strings lexicographically in Python using comparison operators like '<', '>', '==', '<=', and '<=. Lexicographic comparison is the process of comparing two strings based on their alphabetical order.

string1 = "application"
string2 = "apple"

if string1 < string2:
    print(string1, "comes before", string2)
elif string1 > string2:
    print(string2, "comes before", string1)
else:
    print("The two strings are equal")


s = 'a'

# s[0:] will be 'a'
# s[1:] will be ''
# s[2:] will be '',    NO EXCEPTION happen
s[0:]
s[2:]

s = 'help'
s.upper()
s.lower()


s = "a b   c  d  f\tg h"
s = s.replace(' ', '').replace('\t', '')
print(s)

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




