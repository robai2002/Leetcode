class Solution:
    def binaryGap(self, n: int) -> int:
        ans  = 0
        c = -30
        x = 1
        while x<=n:
            if n&x:
                ans = max(ans,c)
                c= 1
            else:
                c+= 1
            x<<=1
        return ans
