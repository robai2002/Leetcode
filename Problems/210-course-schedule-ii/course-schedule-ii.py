class Solution:
    def findOrder(self, n: int, c: List[List[int]]) -> List[int]:
        adj = [set() for i in range(n)]
        deg = [0]*n
        ans = []
        for l in c:
            adj[l[1]].add(l[0])
            deg[l[0]]+=1
        for i in range(n):
            if not deg[i]:
                ans.append(i)
        i = 0
        while i<len(ans):
            for x in adj[ans[i]]:
                if not deg[x]:
                    continue
                deg[x] -=1
                if not deg[x]:
                    ans.append(x)
            i +=1
        if len(ans)==n:
            return ans
        return []
