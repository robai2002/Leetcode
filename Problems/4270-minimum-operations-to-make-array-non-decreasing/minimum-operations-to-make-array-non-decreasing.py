class Solution:
    def minOperations(self, nums: list[int]) -> int:
        result = 0
        prev = -1
        for num in nums:
            if prev > num:
                result += prev - num
            prev = num

        return result