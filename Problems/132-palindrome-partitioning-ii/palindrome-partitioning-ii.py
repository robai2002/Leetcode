class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [[0 for i in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n-i):
                if i==0 or (s[j] == s[i+j] and (dp[j+1][i+j-1] or i == 1)):
                    dp[j][i+j] = 1
                else:
                    dp[j][i+j] = 0
        
        @cache
        def minPalindromes(ind: int) ->int:
            if ind ==n:
                return -1
            
            cut = n+5
            for i in range(ind,n):
                if dp[ind][i]:
                    cut = min(cut,minPalindromes(i+1))
            return cut + 1
        
        return minPalindromes(0)
