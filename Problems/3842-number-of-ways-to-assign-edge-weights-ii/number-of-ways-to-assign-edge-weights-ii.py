class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        n = len(edges) + 2
        graph = [[] for i in range(n)]
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)

        depth = [-1 for i in range(n)]
        anc = [[-1 for i in range(31)] for i in range(n)]

        def dfs(node: int,par: int,dpt: int) ->None:
            depth[node] = dpt
            anc[node][0] = par
            for x in graph[node]:
                if x!=par:
                    dfs(x,node,dpt+1)
            return 

        def makeanc(node: int)-> None:
            for i in range(30):
                x = anc[node][i]
                if x!= -1:
                    anc[node][i+1] = anc[x][i]
            for x in graph[node]:
                if x!=anc[node][0]:
                    makeanc(x)


        dfs(1,-1,0)
        makeanc(1)

        def upword(node: int,n: int) -> int:
            x = 0
            while n:
                if n&1:
                    node = anc[node][x]
                x += 1
                n//=2
            return node

        def lca(x: int,y: int) -> int:
            if x== y:
                return x
            if anc[x][0] == anc[y][0]:
                return anc[x][0]
            p = 0 
            while anc[x][p+1]!= anc[y][p+1]:
                p += 1
            return lca(anc[x][p],anc[y][p])
            
                
                
        ans  = []
        for x,y in queries:
            if x == y:
                ans.append(0)
                continue
            if depth[x]<depth[y]:
                x,y = y,x
            z = depth[x] - depth[y]
            w = depth[x] +depth[y]
            x = upword(x,z)
    
            l = lca(x,y)
            if l == -1:
                ans.append(0)
            else:
                w -= 2*depth[l]
                ans.append(pow(2,w-1,10**9+7))
        return ans
        