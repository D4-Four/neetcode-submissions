class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        sorts = sorted(s)
        sortt = sorted(t)
        for i in range(len(s)):
            if sorts[i] != sortt[i]:
                return False
        return True