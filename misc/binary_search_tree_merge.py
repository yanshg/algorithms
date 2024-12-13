'''
1305. All Elements in Two Binary Search Trees 

Given two binary search trees root1 and root2, return a list containing all the integers from both trees sorted in ascending order.

'''

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.val} -> ({self.left}, {self.right})"
    
def merge_bst_trees(root1, root2) -> list[int]:

    def inorder(root):
        if not root:
            return []
        
        return inorder(root.left) + [ root.val ] + inorder(root.right)
    
    list1 = inorder(root1)
    list2 = inorder(root2)

    result = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[1] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
            
    result.extend(list1[i:])
    result.extend(list2[j:])

    return result

root1 = TreeNode(2, TreeNode(1), TreeNode(4))
root2 = TreeNode(1, TreeNode(0))
print(merge_bst_trees(root1, root2))