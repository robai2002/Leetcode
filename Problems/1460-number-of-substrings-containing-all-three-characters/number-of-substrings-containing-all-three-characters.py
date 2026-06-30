class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans = 0 
        mp = dict()
        for ind,ch in enumerate(s):
            mp[ch] = ind
            z = min([mp.get('a',-1),mp.get('b',-1),mp.get('c',-1)])
            ans += z + 1
        return ans
        