class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: (-x[0],x[1]))
        n,ans = len(points),0
        for ind,(_,v) in enumerate(points):
            y = 1<<31
            for j in range(ind+1,n):
                if y>points[j][1]>=v:
                    ans += 1
                    y = points[j][1]
        return ans
        