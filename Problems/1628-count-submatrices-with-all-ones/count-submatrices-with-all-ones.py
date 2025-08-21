from typing import List

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        col = len(mat[0])
        h, res = [0] * col, 0

        for row in mat:
            memo = []

            for i in range(col):
               
                h[i] = (row[i] == 1) * (h[i] + 1)

                while memo and h[i] < h[memo[-1][0]]:
                    memo.pop()

                ct = (i - memo[-1][0]) * h[i] + memo[-1][1] if memo else h[i] * (i + 1)

                res += ct
                memo.append((i, ct))

        return res
