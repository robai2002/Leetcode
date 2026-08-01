class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[0]*n for i in range(n+2)]
        for k in range(n):
            for i in range(n-k):
                if k == 0:
                    dp[i][i] = nums[i]
                else:
                    dp[i][i+k] = max(nums[i]-dp[i+1][i+k],nums[i+k] - dp[i][i+k-1])

        return dp[0][n-1]>=0