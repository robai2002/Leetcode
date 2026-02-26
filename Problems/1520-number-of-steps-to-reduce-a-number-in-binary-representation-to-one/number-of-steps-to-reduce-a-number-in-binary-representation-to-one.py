class Solution:
    def numSteps(self, s: str) -> int:
        x = '0'
        ans = 0
        for ch in reversed(s[1:]):
            if ch == x:
                ans += 1
            else:
                ans += 2
                x = '1'
            #print(ch,x,ans)
        #print(x,ans)
        if x=='1':
            ans += 1

        return ans
        