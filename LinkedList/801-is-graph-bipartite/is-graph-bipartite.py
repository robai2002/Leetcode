class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        a = [0]*n
        def dfs(node: int,k: int) -> bool:
            if a[node]:
                return a[node] == k
            a[node] = k
            for v in graph[node]:
                if not dfs(v,-k):
                    return False

            return True
        for i in range(n):
            if not a[i] and not dfs(i,1):
                return False
        return True

            