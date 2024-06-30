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
    #    for j in range(i//2, 0, -1):
    #        if i % j == 0:
    #            DP[i] = DP[j] + i // j
    #            break

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