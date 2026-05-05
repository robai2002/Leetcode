# base solution

class Solution:
    def longestPalindromicSubsequence(self, s: str, k: int) -> int:
        @cache
        def calc(a, b):
            delta = abs(ord(a) - ord(b))
            return min(delta, 26 - delta)
        
        @cache
        def dp(i, j, k):
            if i > j:
                return 0
            if i == j:
                return 1
            if s[i] == s[j]:
                return 2 + dp(i + 1, j - 1, k)
            
            result = 0
            if (current := calc(s[i], s[j])) <= k:
                result = 2 + dp(i + 1, j - 1, k - current)
            
            return max(
                result,
                dp(i + 1, j, k),
                dp(i, j - 1, k),
            )
        
        return dp(0, len(s) - 1, k)