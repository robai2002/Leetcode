class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        
        n = len(dungeon)
        m = len(dungeon[0])
        dp = [math.inf] * (m+ 1)
        dp[m-1] = 1
        for i in reversed(range(n)):
            for j in reversed(range(m)):
                dp[j] = min(dp[j], dp[j + 1]) - dungeon[i][j]
                dp[j] = max(dp[j], 1)

        return dp[0]