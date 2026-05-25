class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        dp = [0 for i in range(n+3)]
        dp[0] = 1
        dp[1] = -1
        for ind,ch in enumerate(s):
            if ch == '0' and dp[ind]>0:
                if ind+minJump<n:dp[ind+minJump] += 1
                if ind+maxJump<n:dp[ind+maxJump+1] -= 1
            
            dp[ind+1] +=dp[ind]

        
        return s[-1]=='0' and dp[n-1]>0
        