"""

This question was asked by Google.

Given an integer n and a list of integers l, write a function that randomly generates a number from 0 to n-1 that isn't in l (uniform).

"""

import random
from collections import defaultdict

def generate_number(n, excludes):
    r = random.randrange(n)
    return r if r not in excludes else generate_number(n, excludes)

n,excludes = 10,{1,4,5,6}

error_tolerance = 0.005
expected_prob = round(1.0/(n-len(excludes)), 3)

num_experiments = 10000
results = defaultdict(int)
for i in range(num_experiments):
    results[generate_number(n,excludes)] += 1

for num in results:
    prob = round(float(results[num])/num_experiments, 3)
    print("num: ", num, "probs: ", prob)
    assert expected_prob-error_tolerance <= prob <= expected_prob+error_tolerance
