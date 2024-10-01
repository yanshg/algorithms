'''
The “Remove All Adjacent Duplicates in String II” problem involves removing groups of k adjacent, identical characters from a string until no more such groups exist. Here’s a Python solution using a stack to efficiently manage the removal process:
'''

def remove_duplicates(s, k):
    stack = []
    
    for char in s:
        if stack and stack[-1][0] == char:
            stack[-1][1] += 1
            if stack[-1][1] == k:
                stack.pop()
        else:
            stack.append([char, 1])
    
    result = ''.join(char * count for char, count in stack)
    return result

# Example usage
s = "deeedbbcccbdaa"
k = 3
print(remove_duplicates(s, k))  # Output: "aa"
