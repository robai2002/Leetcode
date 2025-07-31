class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        ans = set()
        curs = set()
        for a in arr:
            ns = {a|v for v in curs}
            ns.add(a)
            ans.update(ns)
            curs = ns
        return len(ans)


                    