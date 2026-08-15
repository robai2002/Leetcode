class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        ans = 0
        if not any(nums):return 0
        for num in nums:
            ans^=num
        return len(nums) if ans>0 else len(nums)-1
        