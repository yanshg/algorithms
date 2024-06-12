def has_path_sum(root, target):
    if not root: 
        return False
    
    if not root.left and not root.right:
        return root.val == target
    
    target -= root.val
    return has_path_sum(root.left, target) or \
        has_path_sum(root.right, target)

def get_all_path_sum(root, target):
    res = []

    def dfs(root, target, path=[], res=[]):
        if not root: 
            return
        
        if not root.left and not root.right:
            if root.val == target:
                res += [ path + [ root.val ] ]
                return
            
        target -= root.val
        path.append(root.val)
        dfs(root.left, target, path, res)
        dfs(root.right, target, path, res)
        path.pop()
 
    dfs(root, target, [], res)
    return res

        