'''
To remove all adjacent duplicates in a string, you can use a stack-based approach. This method efficiently handles the removal of adjacent duplicates by leveraging the Last-In-First-Out (LIFO) property of stacks.
'''

def remove_adjacent_duplicates(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)

# Example usage
s = "abbaca"
print(remove_adjacent_duplicates(s))  # Output: "ca"
