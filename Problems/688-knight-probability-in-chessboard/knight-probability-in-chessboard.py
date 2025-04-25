class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:

        dp = [[[0] * (k + 1) for _ in range(n)] for _ in range(n)]
        moves = [(-2,1),(-2,-1),(2,1),(2,-1),(1,2),(1,-2),(-1,-2),(-1,2)]

        dp[row][column][0] = 1

        for step in range(1,k+1):
            for i in range(n):
                for j in range(n):
                   
                    for x,y  in moves:
                        x += i
                        y += j
                        
                        if 0<=x<n and 0<=y<n:
                            dp[i][j][step] += 0.125 * dp[x][y][step - 1]
                           
        ans = 0
        for i in range(n):
            for j in range(n):
                ans += dp[i][j][k]        
        return ans