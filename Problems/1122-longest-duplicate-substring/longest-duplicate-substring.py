class Solution:
    def longestDupSubstring(self, s: str) -> str:

        def robin_karp(v):
            mod = 10**9+7
            base = 256
            h = pow(base,v-1,mod)
            m  = defaultdict()
            window = 0
            for i,c in enumerate(s):
                if i >= v:
                    window = ((window-ord(s[i-v])*h)*base + ord(c))%mod
                else:
                    window = (window*base + ord(c))%mod

                if window in m and s[i-v+1:i+1] == s[m[window]:m[window]+v]:
                    return s[i-v+1:i+1]

                if i>=v-1:
                    m[window] = i-v+1
            return None





        l,h = 0,len(s)
        ans = ""
        while l<h:
            mid = (l+h+1)//2
            res = robin_karp(mid)
            if not res:
                h = mid - 1
            else:
                ans = res
                l = mid
   
        return ans