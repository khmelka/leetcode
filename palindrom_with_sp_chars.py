import re

def is_palindrome(s: str) -> bool:
        s = re.sub(r'[^A-Za-z0-9]+', '', s).lower()
        return True if s == s[::-1] else False
        
print(is_palindrome("A man, a plan, a canal: Panama"))