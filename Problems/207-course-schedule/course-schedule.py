class Solution:
    def canFinish(self, n: int, p: List[List[int]]) -> bool:
        adj= [set() for i in range(n)]
        depend = [0]*n

        def dfs(node):
            print(node)
            if depend[node]==2:
                return True
            if not depend[node]:
                return False
            depend[node]=2
            for i in adj[node]:
                if dfs(i):
                    return True
            depend[node] = 0
            return False


        for l in p:
            adj[l[0]].add(l[1])
            depend[l[0]]=1

        for i in range(n):
            if depend[i] !=1:
                continue
            elif dfs(i):
                return False 
        return True