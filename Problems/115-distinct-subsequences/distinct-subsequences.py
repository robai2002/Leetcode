class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m , n = len(s),len(t)
        dp = [0 for _ in range(n+1)]
        dp[0] = 1
        for c in s:
            for i in reversed(range(n)):
                if c == t[i]:
                    dp[i+1] += dp[i]
            
        return dp[-1]