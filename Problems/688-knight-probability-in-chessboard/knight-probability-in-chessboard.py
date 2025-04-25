class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        if k == 0:
            return 1
        
        @cache
        def dp(i, j, ml):

            if i < 0 or i>= n or j < 0 or j >= n:
                return 0
            if ml == 0:
                return 1
            
            return (
                dp(i+1, j+2, ml - 1) +
                dp(i-1, j+2, ml - 1) +
                dp(i+2, j+1, ml - 1) +
                dp(i+2, j-1, ml - 1) +
                dp(i+1, j-2, ml - 1) +
                dp(i-1, j-2, ml - 1) +
                dp(i-2, j+1, ml - 1) +
                dp(i-2, j-1, ml - 1)  

            )/8

        return dp(row, column, k) 