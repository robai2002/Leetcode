class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0 
        for ind,ch in enumerate(s,1):
            ans += (ord('z')-ord(ch)+1)*ind
        return ans
        