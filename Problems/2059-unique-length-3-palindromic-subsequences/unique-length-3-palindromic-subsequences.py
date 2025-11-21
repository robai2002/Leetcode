class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first = {}
        last = {}


        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i

        ans = 0
        
        for ch in first:
            l, r = first[ch], last[ch]
            if r - l >= 2:
                ans += len(set(s[l+1:r]))

        return ans
