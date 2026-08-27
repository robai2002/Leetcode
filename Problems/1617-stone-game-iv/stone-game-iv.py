class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        imp = [False for i in range(n+1)]
        imp[1] = True
        for i in range(n+1):
            j = 1
            while j*j<=i:
                if not imp[i-j*j]:
                    imp[i] = True
                    break
                j += 1
        return imp[n]
        