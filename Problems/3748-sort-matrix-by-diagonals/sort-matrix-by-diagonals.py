from typing import List

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])

       
        def _heapify(x: int, y: int, l: int, i: int,t):
            left, right, largest = 2 * i + 1, 2 * i + 2, i

            if left < l and (grid[x + left][y + left] > grid[x + largest][y + largest])==t:
                largest = left
            if right < l and (grid[x + right][y + right] > grid[x + largest][y + largest])==t:
                largest = right

            if largest != i:
                grid[x + i][y + i], grid[x + largest][y + largest] = grid[x + largest][y + largest], grid[x + i][y + i]
                _heapify(x, y, l, largest,t)

        
        def heapsort(x: int, y: int,t):
            l = min(n - x, m - y) 

           
            for i in reversed(range(l // 2)):
                _heapify(x, y, l, i,t)

            print(x,y,l)
          
            for i in reversed(range(l)):
                grid[x][y], grid[x + i][y + i] = grid[x + i][y + i], grid[x][y]
                _heapify(x, y, i, 0,t)

        
        for i in range(n):
            heapsort(i, 0,False)
        for j in range(1, m):
            heapsort(0, j,True)

        return grid
