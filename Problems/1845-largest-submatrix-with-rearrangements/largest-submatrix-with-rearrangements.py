class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    matrix[i][j] = matrix[i-1][j] +1 if i>0 else 1
        for i in range(len(matrix)):
            matrix[i].sort(reverse = True)
            for j in range(len(matrix[0])):
                ans = max(ans,matrix[i][j]*(j+1))
        return ans

        


                    
        