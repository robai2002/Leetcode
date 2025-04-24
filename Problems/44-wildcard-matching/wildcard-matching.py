class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        m = {}
        def solve(a: int,b: int,text: str,pattern: str) ->bool:
            if a<0 and b<0:
                return True
            if b<0 and a>=0:
                return False
            if (a,b) in m:
                return m[(a,b)]
            if a<0 and b>=0:
                return all(c == '*' for c in pattern[:b+1])
            m[(a,b)] = False
            if  text[a] == pattern[b] or pattern[b] == '?':
                m[(a,b)] = solve(a-1,b-1,text,pattern)
            if pattern[b] == '*':
                m[(a,b)] = solve(a-1,b,text,pattern) or solve(a,b-1,text,pattern)
            return m[(a,b)]


        return solve(len(s)-1,len(p)-1,s,p)
