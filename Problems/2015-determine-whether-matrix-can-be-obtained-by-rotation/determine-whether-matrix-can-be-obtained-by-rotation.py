class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        
        a,b,c,d = True, True, True, True

        n = len(mat)
        for i in range(n):
            for j in range(n):
                if mat[i][j]!=target[i][j]: a = False
                if mat[j][n-1-i]!= target[i][j]: b= False
                if mat[n-1-j][i]!= target[i][j]:c = False
                if mat[n-1-i][n-1-j] != target[i][j]:d = False
        return a|b|c|d
        