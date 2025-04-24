class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for i in range(n)]
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        par = [0]*n
        val = [0]*n
        descendant = [1]*n
        ans = [0]*n
        z = 0
        def dfs(node: int,p: int) -> None:
            par[node] = p 
            x,y = 0,0
            for v in graph[node]:
                if v!= p:
                    dfs(v,node)
                    descendant[node] +=descendant[v]
                    val[node] += val[v] + descendant[v]
            return 
        def ans_maker(node: int,p: int) -> None:
            if p!= -1:
                val[node] = val[p]+ n - 2*descendant[node]
            for v in graph[node]:
                if v!=p:
                    ans_maker(v,node)
            return 
        dfs(0,-1)
        ans_maker(0,-1)

        return val