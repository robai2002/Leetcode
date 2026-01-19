class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        ind  = 0 
        ans = []
        n = len(s)
        for i,ch in enumerate(s):
            if s[ind]!=ch :
                if i-ind>2:
                    ans.append([ind,i-1])
                ind = i
        if n-ind>2:ans.append([ind,n-1])
        return ans

        