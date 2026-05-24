class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        n = nums.count(0)
        return n - nums[-n:].count(0)
        