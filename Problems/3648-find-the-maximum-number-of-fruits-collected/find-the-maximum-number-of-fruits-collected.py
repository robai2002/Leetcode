class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)
        ans = 0
        for i in range(n):
            ans += fruits[i][i]
            fruits[i][i] =0


        dp = deepcopy(fruits)
        for i in range(1,n):
            l = max(n-i-1,(n+1)//2)
            for j in range(l,n):
                x = 0
                if j<n-1:
                    x = dp[i-1][j+1]
                if j>n-i-1:
                    x = max(x,dp[i-1][j])
                if j-1>=(n+1)//2 and j-1>n-i-1:
                    x = max(x,dp[i-1][j-1])
                # print(i,j,x)
                dp[i][j] += x
        ans += dp[-1][-1]
        

        dp = deepcopy(fruits)
        for i in range(1,n):
            l = max(n-i-1,(n+1)//2)
            for j in range(l,n):
                x = 0
                if j<n-1:
                    x = dp[j+1][i-1]
                if j>n-i-1:
                    x = max(x,dp[j][i-1])
                if j-1>=(n+1)//2 and j-1>n-i-1:
                    x = max(x,dp[j-1][i-1])
                dp[j][i] += x
                # print(j,i,x)
        ans += dp[-1][-1]
        # print(dp)
        return ans
                
        
