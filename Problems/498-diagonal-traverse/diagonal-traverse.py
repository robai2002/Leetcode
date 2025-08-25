class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans = []
        n = len(mat)
        m = len(mat[0])

        for k in range(n+m-1):
            if k&1:
                for i in reversed(range(min(m,k+1))):
                    x = k - i
                #print(k,i,x)
                    if x>=n:
                        break
                    ans.append(mat[x][i])
            
            else:
                for i in reversed(range(min(n,k+1))):
                    x = k-i
                    if x>=m:
                        break
                    ans.append(mat[i][x])
        return ans