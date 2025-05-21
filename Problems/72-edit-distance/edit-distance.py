class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n,m = len(word1),len(word2)
        dp = [[-1 for _ in range(m+1)] for _ in range(n+1)]
        def get_ans(i,j):
            if i==n:
                return m-j
            if j==m:
                return n-i
            if dp[i][j]>=0:
                return dp[i][j]
            if word1[i] == word2[j]:
                dp[i][j] =  get_ans(i+1,j+1)
            else:              # replace             delete         insert
                dp[i][j] = min(get_ans(i+1,j+1),get_ans(i,j+1),get_ans(i+1,j))+1
            return dp[i][j]

        return get_ans(0,0)