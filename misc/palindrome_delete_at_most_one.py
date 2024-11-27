"""
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome
"""

def is_palindrome(s: str, left: int, right: int) -> bool:
    while left < right:
        if s[left] != s[right]:
            return False
        else:
            left += 1
            right -= 1
    return True

def make_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return is_palindrome(s, left + 1, right) or is_palindrome(s, left, right - 1)
        
    return True