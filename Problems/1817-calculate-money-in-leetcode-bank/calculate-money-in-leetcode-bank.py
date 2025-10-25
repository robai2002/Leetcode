class Solution:
    def totalMoney(self, n: int) -> int:
        w = n//7
        ans = (w*(w-1)//2)*7 + w*28
        m = n%7
        ans+= m*w+ (m*(m+1))//2
        return ans

        