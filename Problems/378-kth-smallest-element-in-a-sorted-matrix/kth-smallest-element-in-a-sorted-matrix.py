class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        m = len(matrix[0])
        
        def heapify(ind: int, limit: int) -> None:
            x,y = ind//m,ind%m
            lx,ly = (ind*2+1)//m,(ind*2+1)%m
            rx,ry = (ind*2+2)//m,(ind*2+2)%m
            if ind*2+1<limit and matrix[x][y] < matrix[lx][ly]:
                x,y = lx,ly
            if ind*2+2<limit and matrix[x][y] < matrix[rx][ry]:
                x,y = rx,ry
            if x*m +y != ind:
                matrix[ind//m][ind%m],matrix[x][y] = matrix[x][y],matrix[ind//m][ind%m]
                heapify(x*m+y,limit)



        def heapsort() ->None:
            for i in reversed(range((n*m)//2)):
                heapify(i,n*m)
            print(matrix)
            for i in reversed(range(n*m)):
                x,y = i//m,i%m
                matrix[x][y],matrix[0][0] = matrix[0][0],matrix[x][y]
                heapify(0,i)
          
        heapsort()
        k -= 1
        return matrix[k//m][k%m]