class Solution:
    def sumAndMultiply(self, n: int) -> int:
        ans = 0 
        x = 1
        y = 0
        while n:
            y+= n%10
            if n%10>0:
                ans += x*(n%10)
                x *= 10
            n//=10
        return ans*y

        