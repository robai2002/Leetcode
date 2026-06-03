class Solution:
    def earliestFinishTime(self, l: List[int], ld: List[int], w: List[int], wd: List[int]) -> int:
        n,m = len(l),len(w)
        x,y = min(l[i]+ld[i] for i in range(n)),min(w[i]+wd[i] for i in range(m))
        ans = 10**10
        for i in range(n):
            ans = min(max(y,l[i])+ld[i],ans)
        for i in range(m):
            ans = min(max(x,w[i])+wd[i],ans)
        return ans
        