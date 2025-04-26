class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        x = len(text1) + 1
        y = len(text2) + 1
        dp = [[0] * y for _ in range(x)]  # Correct initialization of dp array

        for i in range(1, x):
            for j in range(1, y):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[x - 1][y - 1]