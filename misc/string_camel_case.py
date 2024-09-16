
camel_case_str = "MyVariableName"

res = []

left=0
for right,c in enumerate(camel_case_str):
    if c.isupper() and right > left:
        res += [ camel_case_str[left:right] ]
        left = right
res += [ camel_case_str[left:] ]

print(' '.join(res))
