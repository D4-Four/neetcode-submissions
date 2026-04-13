class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zero_count = 0
        for n in nums:
            if n == 0:
                zero_count += 1
            else:
                total *= n

        result = [0] * len(nums)
        # If more than one zero, all products are zero
        if zero_count > 1:
            return result

        for i, v in enumerate(nums):
            if zero_count == 1:
                # Only one zero in the array
                if v == 0:
                    result[i] = total
                else:
                    result[i] = 0
            else:
                # No zeros
                result[i] = total // v
        return result