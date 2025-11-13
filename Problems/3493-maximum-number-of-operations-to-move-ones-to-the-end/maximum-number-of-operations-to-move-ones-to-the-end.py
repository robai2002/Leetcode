class Solution:
    def maxOperations(self, s: str) -> int:
        ans = 0
        x = 0
        y = 0
        for ch in s:
            if ch =='1':
                x += 1
                y = 0
            elif y==0:
                y = 1
                ans += x
        return ans
        