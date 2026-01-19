class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        m = defaultdict(list)
        for s in allowed:
            m[s[:2]].append(s[2])
        @cache
        def solve(s, curr):
            if len(s) == 1:
                return True
            if len(curr)==len(s)-1:
                return solve(curr, "")
            ret = False
            for a in m[s[len(curr):len(curr)+2]]:
                ret = ret or solve(s, curr+a)
            return ret
        return solve(bottom, "")