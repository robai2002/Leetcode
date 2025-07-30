class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        m = max(nums)
        x = 0
        ans = 0
        for num in nums:
            if m&num == m:
                x += 1
            else:
                x = 0
            ans = max(x,ans)
        return ans
        