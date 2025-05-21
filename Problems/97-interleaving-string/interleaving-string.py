# Naive backtracking
# node -> pick how many characters from s1 or s2
# Then alternating picking from s1 and s2 and see if we can complete s3


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        n, m = len(s1), len(s2)
        @lru_cache(maxsize=None)
        def dp(i, j):
            nonlocal s1, s2, s3, n, m

            k = i + j

    
            if i == n and j == m:
                return True


           
            # print(i, j, k)
            if i <= n - 1 and s1[i] == s3[k] and dp(i + 1, j):
                return True
            
            if j <= m - 1 and s2[j] == s3[k] and dp(i, j + 1):
                return True

            return False

        if n + m != len(s3):
            return False

        return dp(0, 0)



            