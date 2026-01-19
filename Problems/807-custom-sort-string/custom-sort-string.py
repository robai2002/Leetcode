class Solution:
    def customSortString(self, order: str, s: str) -> str:
        l = list(s)
        mp = dict()
        for ind,ch in enumerate(order,start = 1):
            mp[ch] = ind
        l.sort(key =lambda x: mp.get(x,0))
        
        return "".join(l)
