class Solution:
    def shortestPalindrome(self, s: str) -> str:
        suffix,prefix = 0,0
        base,power = 29,1
        last_ind = 1
        mod = 10**9+7
        for i,c in enumerate(s):
            char = ord(c)-ord('a') + 1
            prefix = (prefix * base) % mod
            prefix = (prefix + char) % mod
            
            suffix = (suffix + char* power) % mod
            power = (power * base) % mod

            if prefix == suffix:last_ind = i + 1
  
        suffix = s[last_ind:]
        
        return suffix[::-1] + s
