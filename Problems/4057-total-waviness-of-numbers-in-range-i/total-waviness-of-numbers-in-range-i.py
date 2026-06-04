N = 10**5+2
dp= [0 for i in range(N)]
f = [0 for i in range(N)]
for i in range(100,N):
    x,y,z = i%10,(i//10)%10,(i//100)%10
    f[i] = f[i//10]
    if y<min(x,z) or y>max(x,z):f[i] += 1
    dp[i]=dp[i-1] + f[i]

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        return dp[num2] - dp[num1-1]