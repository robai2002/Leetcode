class Solution:
    def almostPalindromic(self, s: str) -> int:
        ln = len(s)

        # this works by expanding the current longest substing centered at l,r
        # skip tells if we can skip a character or not
        def recursive(l,r,skip):
            if l < 0 or r == ln : return 0 if l<0 and r==ln else skip
            res = 0
            if s[l] == s[r]:
                res = max(res,(2 if l<r else 1) + recursive(l-1,r+1,skip)) 
            else:
                if skip:
                    res = max(res,1 + recursive(l-1,r,0))  # skiping s[l] and expand further
                    res = max(res,1 + recursive(l,r+1,0))  # skipping s[r] and expand further
            return res

        res = 0
        for i in range(ln):
            a = max(recursive(i,i,1),res)                           # centered at i only
            b = max(recursive(i,i+1,1), res) if i < ln-1 else 0     # centered at i, i+1 both
            res = max(a,b)
            
        return res
