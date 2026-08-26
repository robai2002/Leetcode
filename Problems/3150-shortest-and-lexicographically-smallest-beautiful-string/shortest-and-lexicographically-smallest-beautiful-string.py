class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        x,y,c = 0,0,0
        ans = ""
        for ind,ch in enumerate(s,1):
            if ch ==  '1':
                c += 1
            while c>k:
                if s[x]=='1':
                    c -= 1
                x += 1
            while x<ind and s[x]=='0': x+= 1
            if k==c:
                y = s[x:ind]
                if not ans or len(y)<len(ans) or (len(ans)==len(y) and y<ans):
                    ans = y 
        return ans
        