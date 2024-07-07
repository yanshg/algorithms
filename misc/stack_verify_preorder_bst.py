'''
Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree.

You may assume each number in the sequence is unique.

Follow up:
Could you do it using only constant space complexity?
'''

def verify_preorder_bst(nums):
    min = float('-inf')
    stack = []
    for num in nums:
        if num < min:
            return False
        
        while stack and stack[-1] < num:
            min = stack.pop()
        stack.append(num)

    return True

nums = [ 6, 4, 3, 5, 9, 7, 11]
print(verify_preorder_bst(nums))