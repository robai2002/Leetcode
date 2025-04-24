class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        b = s[::-1]
        n = len(b)+1
        dp = [[0 for i in range(n)]for j in range(n)]
        for i in range(1,n):
            for j in range(1,n):
                if s[i-1]==b[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        
        return dp[-1][-1]
