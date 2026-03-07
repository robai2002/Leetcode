class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s = s + s
        x = 0 
        ans = n
        for ind,ch in enumerate(s,start = 1-n):
            if  ord(ch)%2 == (n-1+ind)&1:
                x += 1
            if ind >=0:
                ans = min(ans,min(x,n-x))
                if ord(s[ind])%2 == ind&1:
                    x -= 1
            #print(ind,ans)
        

        return ans