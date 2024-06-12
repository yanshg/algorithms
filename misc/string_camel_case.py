
camel_case_str = "myVariableName"

res = []

left=0
for right,c in enumerate(camel_case_str):
    if c.isupper():
        res += [ camel_case_str[left:right] ]
        left = right
res += [ camel_case_str[left:] ]

print(' '.join(res))
