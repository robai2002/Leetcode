class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        need = n-1
        ans = 10**10

        par = [i for i in range(n)]

        def find(node: int) ->int:
            if par[node] == node:
                return node
            return find(par[node])
        
        edges.sort(key = lambda l:(-l[3],-l[2]))
        print(edges)

        for u,v,c,m in edges:
            if need == 0 and m == 1:return -1
            a,b = find(u),find(v)
            if a == b:
                if m== 1:
                    return -1
                continue
            par[b] = a
            need -= 1
            if m == 0 and k>need:
                    k -= 1
                    ans = min(c*2,ans)
                
            else:
                ans = min(c,ans)
            
        if need>0:
            return -1
        return ans
        