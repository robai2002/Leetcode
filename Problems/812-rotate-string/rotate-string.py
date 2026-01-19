class Solution:
    def rotateString(self, s: str, pattern: str) -> bool:
        if len(s)!=len(pattern):
            return False
        s = s + s[:-1]
        
        def compute_lps(pattern):
            lps = [0] * len(pattern)
            length = 0  # length of previous longest prefix suffix
            i = 1

            while i < len(pattern):
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps
        
        dp = compute_lps(pattern)

        
        i = 0
        for ch in s:
            while i>0 and ch != pattern[i]:i = dp[i-1]
            if ch == pattern[i]:i+= 1
            if i==len(pattern):
                return True 
            


        return False
        