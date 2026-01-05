class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        d,s,mn=0,0,10**6
        for m in matrix:
            for num in m:
                if num<0:d^=1
                s += abs(num)
                mn = min(2*abs(num),mn)
        return s-mn if d else s
