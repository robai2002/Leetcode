class Solution:
    def largestSquareArea(self, bottomLeft, topRight):
        ans = 0
        
        for i, (l, r) in enumerate(zip(bottomLeft, topRight)):
            for m, n in zip(bottomLeft[i+1:], topRight[i+1:]):
                x = min(r[0], n[0]) - max(l[0], m[0])
                y = min(r[1], n[1]) - max(l[1], m[1])
                
                if x > 0 and y > 0:
                    ans = max(ans, min(x, y))
        
        return ans * ans
