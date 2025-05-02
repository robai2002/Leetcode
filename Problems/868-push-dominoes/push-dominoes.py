class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        dp = [0]*n
        x = 0
        for i in range(n-1,-1,-1):
            if dominoes[i] =='L':
                x = 1
            elif dominoes[i] == 'R':
                x = 0 
            dp[i] = x
            if x:
                x += 1
        x = 0
        ans = []
        
        for i,c in enumerate(dominoes):
            if c == 'R':
                x = 1

            if x == dp[i]:
                ans.append('.')
                x = 0
            
            elif x and (dp[i]==0 or x<dp[i]):
                ans.append('R')
                x +=1
                
            else:
                ans.append('L')
                x = 0
        return ''.join(ans)

        return ''.join(ans)




        
    