class Solution:
    def findLUSlength(self, strs: List[str]) -> int:

        def isSub(x: str,y: str) ->bool:
            if len(x)>len(y):return False
            i,j = 0,0
            while i<len(x) and j<len(y):
                if x[i]==y[j]:i+= 1
                j += 1
            return i == len(x)
        
        strs.sort(key = len, reverse = True)
        n = len(strs)

        for i in range(n):
            p = 1
            for j in range(n):
                if i!=j and isSub(strs[i],strs[j]):
                    p = 0
                    break
            if p:
                return len(strs[i])
        return -1
