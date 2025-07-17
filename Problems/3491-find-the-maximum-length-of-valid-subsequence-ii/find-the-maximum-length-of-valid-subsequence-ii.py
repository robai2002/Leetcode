class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [[0 for i in range(k)] for _ in range(k)]
        ans = 0
        for num in nums:
            num%=k
            for i in range(k):
                dp[i][num] = dp[num][i] + 1
                ans = max(dp[i][num],ans)
        return ans


                 