class Solution:
    def uniqueLetterString(self, s: str) -> int:
        mf = dict()
        ms = dict()
        ans = 0

        for i,ch in enumerate(s):
            if ch not in mf:
                mf[ch] = -1
                ms[ch] = i
            else:
                ans += (ms[ch]-mf[ch])*(i-ms[ch])
                mf[ch],ms[ch] = ms[ch],i
        n = len(s)
        for ch in mf:
            ans += (n-ms[ch])*(ms[ch]-mf[ch])

        return ans

        