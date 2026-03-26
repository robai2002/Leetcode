from typing import List

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        sm = 0
        for row in grid:
            sm += sum(row)
        
        def solve(arr,x) -> bool:
           # print(arr)
            y = 0
            s = set()
            s.add(0)
            
            
            for ind,row in enumerate(arr):
                y += sum(row)
                if ind==0:
                    s.add(row[0])
                    s.add(row[-1])
                elif len(row)>1:
                    s.update(row)
                else:
                    if 2*y-x==row[0]:
                        return True
                
                if  (2*y-x) in s:
                   # print(s,x,y)
                    return True
                if ind==0:
                    s.update(row)
            return False
        
       
        if solve(grid,sm):
            return True
        
      
        if solve(list(reversed(grid)),sm):
            return True
        
       
        transposed = [list(row) for row in zip(*grid)]
        if solve(transposed,sm):
            return True
        

        if solve(list(reversed(transposed)),sm):
            return True
        
        return False