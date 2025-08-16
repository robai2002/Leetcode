class Solution:
    def maximum69Number (self, num: int) -> int:
        s = str(num)
        ans = [] 
        for i,c in enumerate(s):
            if c!='9':
                ans.append('9')
                ans.append(s[i+1:])
                break
            ans.append(c)
        return int("".join(ans))