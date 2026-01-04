class Solution:
    def sumFourDivisors(self, nums):
        def isPrime(x):
            if x < 2:
                return False
            i = 2
            while i * i <= x:
                if x % i == 0:
                    return False
                i += 1
            return True

        res = 0
        for n in nums:
            p = round(n ** (1 / 3))
            if p ** 3 == n and isPrime(p):
                res += 1 + p + p * p + n
                continue

            i = 2
            while i * i <= n:
                if n % i == 0:
                    j = n // i
                    if i != j and isPrime(i) and isPrime(j):
                        res += 1 + i + j + n
                    break
                i += 1
        return res