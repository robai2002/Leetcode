class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        ans = 0
        x = 1<<(k-1)
        mp = dict()
        z = 0
        for ind,ch in enumerate(s,start = -k+1):
            z<<=1
            if ch=='1':
                z += 1
            if ind>=0:
                mp[z] = 1
            z%=x
        return len(mp)==x*2

            