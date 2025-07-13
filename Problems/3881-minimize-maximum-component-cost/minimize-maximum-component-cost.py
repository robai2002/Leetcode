class Solution:
    def minCost(self, n: int, edges: List[List[int]], k: int) -> int:
        edges.sort(key = lambda x:x[2])
        par = [i for i in range(n)]
        def find_par(node)->int:
            if par[node] == node:
                return node
            par[node] = find_par(par[node])
            return par[node]
        mx = 0
        for u,v,w in edges:
            x = find_par(u)
            y = find_par(v)
            if x!=y:
                n -= 1
                mx = max(w,mx)
                par[x] = y 
            if n == k:
                return mx
            
        return 0