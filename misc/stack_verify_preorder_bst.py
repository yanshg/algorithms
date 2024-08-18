'''
Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree.

You may assume each number in the sequence is unique.

Follow up:
Could you do it using only constant space complexity?

思路：前序遍历的规律是数组是先递减然后再递增，所以我们维护一个变量min和单调递减的stack，表示当前最小的数值，如果当前的数小于min则返回false。如果栈顶的数比当前的数小，则将min更新为栈顶的数。


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