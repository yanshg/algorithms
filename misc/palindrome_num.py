# 121 is palindrome number

def is_palindrome_num(num: int) -> bool:
    if num < 10:
        return True
    
    reverse_num = 0
    orig_num = num
    while num:
        reverse_num = reverse_num * 10 + (num % 10)
        num //= 10

    return reverse_num == orig_num

assert is_palindrome_num(121)
assert not is_palindrome_num(87)
assert is_palindrome_num(8)
