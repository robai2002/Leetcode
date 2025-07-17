class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        dp = [-1 for i in range(target+1)]
        dp[0] = 0
        for num in nums:
            for i in reversed(range(target-num+1)):
                if dp[i]<0:
                    continue
                dp[i+num] = max(dp[i+num],dp[i]+1)
        return dp[target]