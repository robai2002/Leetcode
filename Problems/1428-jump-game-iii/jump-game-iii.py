class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        vis = [False for i in range(n)]
        l = [start]
        i = 0
        while i<len(l):
            if arr[l[i]]==0:return True
            x,y = l[i]+ arr[l[i]],l[i]- arr[l[i]]
            if 0<=x<n and vis[x]==False:
                vis[x]= True
                l.append(x)
            if 0<=y<n and vis[y]==False:
                vis[y]= True
                l.append(y)
            i += 1
        return False
        