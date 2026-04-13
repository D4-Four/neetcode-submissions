class Solution:
    def isValid(self, s: str) -> bool:
        bracketlist = []
        matching = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in matching:  # closing bracket
                if not bracketlist or bracketlist.pop() != matching[char]:
                    return False
            else:  # opening bracket
                bracketlist.append(char)
        
        return len(bracketlist) == 0
            