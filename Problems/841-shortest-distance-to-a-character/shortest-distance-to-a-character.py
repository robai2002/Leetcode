class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        ans = [0]*n
        x = -n
        for i,ch in enumerate(s):
            if ch == c:x =i
            ans[i] = i - x
        x = 2*n
        for i in range(n-1,-1,-1):
            if s[i] == c: x = i
            ans[i] = min(ans[i],x-i)
        return ans
        