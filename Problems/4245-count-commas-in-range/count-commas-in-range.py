class Solution:
    def countCommas(self, n: int) -> int:
        x = 3
        ans = 0
        while 10**x<=n:
            ans += n - 10**x + 1
            x += 3
        return ans
        