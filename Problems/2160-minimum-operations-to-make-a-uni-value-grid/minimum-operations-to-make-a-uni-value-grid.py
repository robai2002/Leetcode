class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        l = []
        for g in grid:
            for v in g:
                l.append(v)
        l.sort()
        
        n = len(l)
        g = 0
        ans = 0
        for i in range(n // 2):
            d = l[n - i - 1] - l[i]
            ans += d
            g = gcd(d, g)
        if n % 2 == 1 and n > 1:
            d = gcd(l[n//2]-l[0],l[-1]-l[n//2])
            g= gcd(g,d)
        if ans == 0:
            return ans
        if g%x ==0:
            return ans//x
        return -1
             
