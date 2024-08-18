'''
This problem was asked by Palantir.

The ancient Egyptians used to express fractions as a sum of several terms where each numerator is one. For example, 4 / 13 can be represented as 1 / 4 + 1 / 18 + 1 / 468.

Create an algorithm to turn an ordinary fraction a / b, where a < b, into an Egyptian fraction.
'''

def egypt_fraction(a: int, b: int) -> list:
    # base cases
    if a == 0:
        return []
    
    f = b // a
    if b % a == 0:
        return [ f ]

    f += 1
    return [ f ] + egypt_fraction(a * f - b, b * f)

#print(egypt_fraction(-4, 13))
assert egypt_fraction(4, 13) == [ 4, 18, 468]



