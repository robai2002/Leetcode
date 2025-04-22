class Solution:
    def numSquares(self, n: int) -> int:
        def is_square(n):
            return int(n**(1/2))**2 == n
        
        if is_square(n): return 1
        
        while n % 4 == 0: n >>= 2

        if n % 8 == 7: return 4

        sqrt_from_n = int(n**(1/2))
        for i in range(1, sqrt_from_n + 1):
            if is_square(n - i*i): return 2
        
        return 3