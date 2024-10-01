'''
Given an absolute path for a file (Unix-style), simplify it.

For example,
path="/home/", =>"/home"
path="/a/./b/../../c/", =>"/c"

Corner Cases:

Did you consider the case where path ="/../"?
In this case, you should return"/"

Another corner case is the path might contain multiple slashes
'/'together, such as"/home//foo/"In this case, you should ignore redundant slashes and return
"/home/foo".

'''

def simplify_path(s):
    if not s:
        return s
    
    res =[]
    skip = 0
    for item in reversed(s.split('/')):
        # must first handle . and blank, to handle case: "/a/./b/../../"
        if item == '' or item == '.':
            continue
        
        if item == '..':
            skip += 1
        elif skip > 0:
            skip -= 1
        else:
            res += [ item ]

    # should not use: res += ['']
    return '/' + '/'.join(reversed(res))

def simplifyPath(path: str) -> str:
    stack = []
    components = path.split('/')
    
    for component in components:
        if component == '' or component == '.':
            continue
        if component == '..':
            if stack:
                stack.pop()
        else:
            stack.append(component)
    
    return '/' + '/'.join(stack)

# Example usage
path = "/a/./b/../../c/"
print(simplifyPath(path))  # Output: "/c"


path = "/a/./b/../../c/"
print("path: ", simplify_path(path))

path = '/../'
print("path: ", simplify_path(path))
