from collections import deque
from typing import List

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows = len(grid)
        columns = len(grid[0])
        seen = set()
        queue = deque()
        seen.add((0, 0, k))
        queue.append((0, (0, 0, k)))
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        target = (rows - 1, columns - 1)

        if k >= rows + columns - 2:
            return rows + columns - 2

        while queue:
            step, (row, col, eliminate) = queue.popleft()
            if (row, col) == target:
                return step

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < rows and 0 <= new_col < columns:
                    new_eliminate = eliminate - grid[new_row][new_col]
                    new_state = (new_row, new_col, new_eliminate)
                    if new_eliminate >= 0 and new_state not in seen:
                        seen.add(new_state)
                        queue.append((step + 1, new_state))
        return -1
