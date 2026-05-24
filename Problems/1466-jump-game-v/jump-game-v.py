class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)

        @cache
        def dfs(i: int) -> int:
            res = 1

            for node in range(i+1,min(i+d+1,n)):
                if arr[node]>=arr[i]:break
                res = max(res,dfs(node)+1)
            for node in range(i-1,max(i-d-1,-1),-1):
                if arr[node]>=arr[i]:break
                res = max(res,dfs(node)+1)
            return res
        
        return max(dfs(i) for i in range(n))