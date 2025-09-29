class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        @cache
        def DP(i: int, j: int) ->int:
            if j<i+2:
                return 0
            
            res = float('inf')
            for k in range(i+1,j):
                res = min(res,values[i]*values[j]*values[k] + DP(i,k) + DP(k,j))
            
            return res

        return DP(0,len(values)-1)