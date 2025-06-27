class Solution:
    def isNumber(self, s: str) -> bool:
        
        def Number(ind: int)-> int:
            x = ind
            while x<len(s) and '0'<=s[x]<='9':
                x += 1
            return x 
        




        n = len(s)
        ind = 0
        if ind<n and s[ind] in '+-':
            ind += 1
            if ind == n:
                return False
        x = Number(ind)
        if x==n:
            return True
        ind = x
        if s[x]=='.':
            ind += 1
            x = Number(ind)
            if x ==ind and (ind<2 or '9'<s[ind-2] or s[ind-2]<'0'):
                return False
            ind = x
        if x==n:
            return True
        if ind>0 and ('0'<=s[ind-1]<='9' or s[ind-1] =='.') and s[ind] in 'eE':
            ind += 1
            if ind<n and s[ind] in "+-":
                ind += 1
            x = ind
            ind = Number(ind)
            if x == ind:
                return False
        
        return n==ind 