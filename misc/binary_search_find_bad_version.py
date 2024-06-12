'''
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions[1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an APIbool isBadVersion(version)which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

'''

def isBadVersion(version):
    if version >= 7:
        return True
    return False

def find_first_bad_version(versions):
    n = len(versions)
    left, right = 0, n - 1
    while left < right:
        mid = left + (right - left)//2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1
    return left

print(find_first_bad_version(range(500)))
    
