class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        x = n-1
        l = []
        for i in range(m-1):
            l.append('.'+'#'*x)
        l.append('.'*n)
        return l