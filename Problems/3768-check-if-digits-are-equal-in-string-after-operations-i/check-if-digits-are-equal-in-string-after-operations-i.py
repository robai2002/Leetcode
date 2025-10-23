class Solution:
    def hasSameDigits(self, s: str) -> bool:
        if len(s) == 2:
            return s[0] == s[1]
        
        ss = ""
        x = int(s[0])
        
        for i in range(1, len(s)):
            y = int(s[i]) 
            x = (x + y)%10 
            ss += str(x) 
            x = y 
        
        return self.hasSameDigits(ss)