class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if len(a)!=len(b):return max(len(a),len(b))
        i,j = 0,0
        while i<len(a) and j<len(b):
            if a[i]  == b[j]: i+=1
            j+=1
        return len(b) if i!=len(a) else -1
        