'''
Initially on a notepad only one character 'A' is present. You can perform two operations on this notepad for each step:

Copy All: You can copy all the characters present on the notepad (partial copy is not allowed).

Paste: You can paste the characters which are copied last time.

Given a number n. You have to get exactly n 'A' on the notepad by performing the minimum number of steps permitted. Output the minimum number of steps to get n 'A'.

Example 1:


Input: 3
Output: 3

Explanation:

Intitally, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.

Note:
Then will be in the range [1, 1000].

'''

def get_keyboards(n):
    # DP[i]: minimum step to get i 'A'

    # Ideas:
    #    base cases:  
    #    DP[0] = 0,  DP[1] = 0, DP[i] = i
    #
    #    for each i from 2 to n
    #        for j in range(i//2, 0, -1):
    #            if i % j == 0:
    #                DP[i] = DP[j] + i // j
    #                break

    DP = list(range(n+1))
    DP[1] = 0

    for i in range(2, n+1):
        for j in range(i//2, 0, -1):
            if i % j == 0:
                DP[i] = DP[j] + i // j
                break

    print(DP)
    return DP[-1]

print(get_keyboards(100))

'''
[0, 0, 2, 3, 4, 5, 5, 7, 6, 6, 7, 11, 7, 13, 9, 8, 8, 17, 8, 19, 9, 10, 13, 23, 9, 10, 15, 9, 11, 29, 10, 31, 10, 14, 19, 12, 10, 37, 21, 16, 11, 41, 12, 43, 15, 11, 25, 47, 11, 14, 12, 20, 17, 53, 11, 16, 13, 22, 31, 59, 12, 61, 33, 13, 12, 18, 16, 67, 21, 26, 14, 71, 12, 73, 39, 13, 23, 18, 18, 79, 13, 12, 43, 83, 14, 22, 45, 32, 17, 89, 13, 20, 27, 34, 49, 24, 13, 97, 16, 17, 14]
14
'''