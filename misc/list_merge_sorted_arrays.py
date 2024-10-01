'''
The “Merge Sorted Array” problem on LeetCode involves merging two sorted arrays into one sorted array. The first array, nums1, has enough space to hold the elements of both arrays.
'''

def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    # Start from the end of nums1 and nums2
    i, j, k = m - 1, n - 1, m + n - 1
    
    # Merge nums2 into nums1
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

# Example usage
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
merge(nums1, m, nums2, n)
print(nums1)  # Output: [1, 2, 2, 3, 5, 6]
