from typing import List

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        mod = 10**9 + 7
  
        dp = [[[0, 0] for _ in range(m)] for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    val = grid[i][j]
                    dp[i][j] = [val, val]
                else:
                 
                    max_val = float('-inf')
                    min_val = float('inf')
                    
                    
                    if i > 0:
                        top_max, top_min = dp[i-1][j]
                        curr_max = top_max * grid[i][j]
                        curr_min = top_min * grid[i][j]
                        max_val = max(max_val, curr_max, curr_min)
                        min_val = min(min_val, curr_max, curr_min)
                    
                   
                    if j > 0:
                        left_max, left_min = dp[i][j-1]
                        curr_max = left_max * grid[i][j]
                        curr_min = left_min * grid[i][j]
                        max_val = max(max_val, curr_max, curr_min)
                        min_val = min(min_val, curr_max, curr_min)
                    
                    dp[i][j] = [max_val, min_val]
    
        result = dp[-1][-1][0]
        
        if result < 0:
            if any(0 in row for row in grid):
                return 0
            return -1
        
        return result % mod