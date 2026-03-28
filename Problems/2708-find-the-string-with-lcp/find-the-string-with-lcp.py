from typing import List

class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        s = [''] * n
        
        ch = 'a'
        for i in range(n):
            
            if s[i]:
                continue
            if ch > 'z':
                return ""
            s[i] = ch
            for j in range(i + 1, n):
                if lcp[i][j] > 0:
                    s[j] = s[i]
            ch = chr(ord(ch) + 1)
        
      
        for i in range(n):
            for j in range(n):
                if s[i] == s[j]:
                    if i == n - 1 or j == n - 1:
                        prevpref = 0
                    else:
                        prevpref = lcp[i + 1][j + 1]
                    prefix = 1 + prevpref
                else:
                    prefix = 0
                if prefix != lcp[i][j]:
                    return ""
        
        return ''.join(s)