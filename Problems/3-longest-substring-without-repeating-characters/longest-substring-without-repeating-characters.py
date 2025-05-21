class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        m = defaultdict(int)
        x = 0
        for i,c in enumerate(s):
            x = max(m[c]+1,x)
            ans = max(ans,i-x+2)
            m[c] = i+1
        return ans
