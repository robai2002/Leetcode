class Solution:
    def maxProduct(self, n: int) -> int:
        l = list(map(int,str(n)))
        l.sort(reverse = True)
        return l[0]*l[1]