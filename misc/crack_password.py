"""
There is a box protected by a password. The password is a sequence of n digits where each digit can be in the range [0, k - 1].

While entering a password, the last n digits entered will automatically be matched against the correct password.

For example, assuming the correct password is "345", if you type "012345", the box will open because the correct password matches the suffix of the entered password.

Return any password of minimum length that is guaranteed to open the box at some point of entering it.

"""

def crackSafe(n, k):
    ans = "0" * (n - 1)
    visits = set()
    for x in range(k ** n):
        current = ans[-n+1:] if n > 1 else ''
        print("current:", current)
        for y in range(k - 1, -1, -1):
            if current + str(y) not in visits:
                visits.add(current + str(y))
                ans += str(y)
                break
    return ans

res=crackSafe(2,2)
print(res)

res=crackSafe(5,3)
print(res)
