import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char for char in s if char.isalnum())
        s = s.lower()
        s = s.strip()
        dec = 0
        for i in range(len(s)//2):
            if s[i] != s[len(s)-(i+1)]:
                return False
        return True