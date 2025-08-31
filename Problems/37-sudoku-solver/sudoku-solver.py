from collections import defaultdict
from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        square = defaultdict(set)
        rows = defaultdict(set)
        column = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    x = int(board[i][j])
                    y = (i // 3) * 3 + (j // 3)
                    rows[i].add(x)
                    column[j].add(x)
                    square[y].add(x)

        def ans(i: int) -> bool:
            if i == 81:
                return True

            r, c = i // 9, i % 9
            if board[r][c] != '.':
                return ans(i + 1)

            s = (r // 3) * 3 + (c // 3)

            for v in range(1, 10):
                if v not in rows[r] and v not in column[c] and v not in square[s]:
                    board[r][c] = str(v)
                    rows[r].add(v)
                    column[c].add(v)
                    square[s].add(v)

                    if ans(i + 1):
                        return True

                    board[r][c] = '.'
                    rows[r].remove(v)
                    column[c].remove(v)
                    square[s].remove(v)

            return False 

        ans(0)
