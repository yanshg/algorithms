'''
This problem was asked by Stitch Fix.

Pascal's triangle is a triangular array of integers constructed with the following formula:

The first row consists of the number 1.
For each subsequent row, each element is the sum of the numbers directly above it, on either side.
For example, here are the first few rows:

    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
Given an input k, return the kth row of Pascal's triangle.

Bonus: Can you do this using only O(k) space?


'''


#  from back to beginning
#  i -> 1,   range(i, 0, -1),    the third argument is step

def pascal_triangle(k):
    DP = [0] * (k+1)
    DP[0] = 1
    for i in range(1, k + 1):
        for j in range(i, 0, -1):
            DP[j] += DP[j-1]
    return DP

print(pascal_triangle(1))
print(pascal_triangle(6))

