class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        x,y=0,0
        d=1
        while n:
            m = n%10
            n //= 10
            if m<2 and n>0:
                m += 10
                n -= 1
            x += (m//2)*d
            y += (m - m//2)*d
            d *= 10
        return [x,y]
        