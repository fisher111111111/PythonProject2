def is_palindrome(s):
    filtered = ''.join(char.lower() for char in s if char.isalnum())
    return filtered == filtered[::-1]


print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("racecar"))                         # True
print(is_palindrome("hello"))                           # False
