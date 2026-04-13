class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        insubstring = set()
        left = 0
        longestSubstring = 0

        for right in range(len(s)):
            # shrink window from the left until no duplicate
            while s[right] in insubstring:
                insubstring.remove(s[left])
                left += 1

            insubstring.add(s[right])
            longestSubstring = max(longestSubstring, right - left + 1)

        return longestSubstring
