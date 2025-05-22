class Solution:
    def searchMatrix(self, matrix, target):
        
                
        i, j = len(matrix) - 1, 0
        while(i >= 0 and i < len(matrix) and j >=0 and j < len(matrix[0])):
            if(matrix[i][j] == target): return True
            if(matrix[i][j] > target):  i -= 1
            if(matrix[i][j] < target):  j += 1              
        return False