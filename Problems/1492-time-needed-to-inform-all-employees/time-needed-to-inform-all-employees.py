class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = [[] for i in range(n+1)]
        for i,v in enumerate(manager):
            graph[v+1].append(i+1)
        
        def dfs(node: int) ->int:
            ans = 0
            for v in graph[node]:
                ans = max(dfs(v),ans)
            ans += informTime[node-1] if node and len(graph[node]) else 0
            return ans 

        return dfs(0)