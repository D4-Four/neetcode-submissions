class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 1
        right = len(numbers)
        for i in range(len(numbers)-1):
            # case 1: left + right > target
            if numbers[left-1] + numbers[right-1] > target:
                right -= 1
            # case 2: left + right < target
            elif numbers[left-1] + numbers[right-1] < target:
                left += 1
            else:
                break
        return [left, right]