class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        visited = [False]*n
        safe = [False]*n
        ans = 0
        def dfs(node: int) ->bool:
            if visited[node]:
                return safe[node]
            visited[node] = True
            b = True
            for v in graph[node]:
                b &= dfs(v)
            safe[node] = b
            return safe[node]


                 

        ans = []
        for i in range(n):
            if not visited[i]:
                dfs(i)
            if safe[i]:
                ans.append(i)
        return ans