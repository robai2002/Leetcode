class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        dp = [-1]*32
        
        for i in reversed(range(len(nums))):
            for b in range(32):
                if nums[i] & (1<<b) : 
                    dp[b] = i
            nums[i] = max(1, max(dp) - i + 1)
        return nums