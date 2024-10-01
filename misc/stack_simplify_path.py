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
