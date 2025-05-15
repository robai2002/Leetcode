class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        l = [i for i in range(n*n)]
        step = [400 for i in range(n*n)]
        for i in range(n):
            x = (n-i-1)*n
            for j in range(n):
                y =  j if (n-i)&1==1 else n-j-1
                y+=x
                l[y] = y if board[i][j] == -1 else board[i][j] -1
                print(y,l[y],board[i][j])
        print(l)


        q = deque()
        q.append([0,0])
     
        while q:
            a,b = q.popleft()
            if a == n*n-1:
                return b
            b += 1
            for i in range(6,0,-1):
                if a+i>=n*n:continue
                i = l[a+i]
                if step[i]>b:
                    step[i] = b
                    q.append([i,step[i]])
        
        return -1
                    


        