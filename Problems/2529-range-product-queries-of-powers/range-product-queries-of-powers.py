class Solution:
    def productQueries(self, n, Q):
        A = list(accumulate([i for i in range(31) if n & (1 << i)])) + [0]
        return [pow(2, A[r] - A[l - 1], 10 ** 9 + 7) for l, r in Q]