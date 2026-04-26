class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        n,m = len(grid),len(grid[0])
        isvisited = [[False]*m for i in range(n)]
        iscycle = [[False]*m for i in range(n)]
        
        def dfs(indx: int,indy: int,parx: int,pary: int) ->bool:
            if indx<0 or indy<0 or indx>=len(grid) or indy>=len(grid[0]):return False
            if parx!=-1 and grid[indx][indy] != grid[parx][pary]:return False
            if iscycle[indx][indy]:return True
            if isvisited[indx][indy]:return False
            iscycle[indx][indy] = isvisited[indx][indy] = True
            nig = [(0,-1),(0,1),(1,0),(-1,0)]
            for x,y in nig:
                x+= indx
                y+= indy
                if x==parx and y==pary:continue
                if dfs(x,y,indx,indy):return True
            
            iscycle[indx][indy] = False
            return False

    
        for i in range(n):
            for j in range(m):
                if not isvisited[i][j] and dfs(i,j,-1,-1):return True
                
        
        return False
