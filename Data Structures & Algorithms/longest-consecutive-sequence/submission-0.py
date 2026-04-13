class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myset = set(nums)
        longest = 0
        for n in nums:
            total = 0
            if (n-1) not in myset:
                while (n+total) in myset:
                    total += 1
                longest = max(total, longest)
        return longest



