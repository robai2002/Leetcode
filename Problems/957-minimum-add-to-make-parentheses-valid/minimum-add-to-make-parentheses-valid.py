class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ans,x = 0,0
        for c in s:
            if c =='(':
                x += 1
            elif x:
                x -= 1
            else:
                ans += 1
        return ans + x