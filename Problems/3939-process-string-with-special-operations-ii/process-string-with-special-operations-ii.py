class Solution:
    def processStr(self, s: str, k: int) -> str:
        length = 0

        for c in s:
            if c.islower():
                length += 1
            elif c=='*' and length>0:
                length -= 1
            elif c == '#':
                length *= 2
        
        if k>=length:
            return '.'
        
        s = s[::-1]
        for c in s:
            if c.islower():
                if k==length -1:
                    return c
                length -= 1
            elif c=='*':
                length += 1
            elif c == '#':
                length//=2
                if k>=length:
                    k -= length
            elif c == '%':
                k = length -1-k
        
        return '.'
 