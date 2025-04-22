class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        par = [-1]*n
        def find_set(v: int) -> int:
            if par[v] == -1:
                return v
            par[v] = find_set(par[v])
            return par[v]
        
        def union_set(x: int,y: int)->bool:
            a = find_set(x)
            b = find_set(y)
            if a != b:
                par[b] = a
            return a==b
        ans = []   
        for a,b in edges:
            if union_set(a,b):
                return [a,b]
