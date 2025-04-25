class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for i in range(n)]
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)

        dp = [[0,0]for i in range(n)]

        def dfs(node: int,par: int) -> int:

            for v in graph[node]:
                if v!=par:
                    dp[node][1] = max(dp[node][1],dfs(v,node))
                if dp[node][0]<dp[node][1]:
                    dp[node] = dp[node][::-1]
            return dp[node][0]+1


        def dfs1(node: int,par: int) ->int:
            x = 0 
            if par!=-1:
                x = dp[par][0] + 1 if dp[par][0]-1!=dp[node][0] else dp[par][1] + 1
         
            if x>dp[node][1]:
                dp[node][1] = x
            if dp[node][0]<dp[node][1]:
                dp[node] = dp[node][::-1]
            x = sum(dp[node])
            for v in graph[node]:
                if v!=par:
                    x = max(dfs1(v,node),x)

            return x
        
        dfs(0,-1)
        x = dfs1(0,-1)

        ans = []
        
        for i,(a,b) in enumerate(dp):
            if a == x-x//2 and b == x//2:
                ans.append(i)
        return ans


