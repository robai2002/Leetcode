class Solution:
    def minimumDeletions(self, s: str) -> int:
        b = 0
        ans = len(s)
        a = s.count('a')
        if a==0:
            return 0
        for ch in s:
            if ch=='a':
                a -=1 
            ans = min(a+b,ans)
            if ch=='b':
                b+= 1
        return ans


        