class Solution:
    def maxFreqSum(self, s: str) -> int:
        m  = defaultdict(int)
        mxv,mxc =0,0
        for c in s:
            m[c] += 1
            if c in "aeiou":
                mxv= max(mxv,m[c])
            else:
                mxc= max(mxc,m[c])
        return mxc+mxv
            