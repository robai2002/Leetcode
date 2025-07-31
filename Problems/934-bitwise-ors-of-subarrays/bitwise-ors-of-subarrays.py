class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        ans = set()
        curs = set()
        for a in arr:
            ns = set()
            for v in curs:
                v|=a
                ns.add(v)
            ns.add(a)
            ans.update(ns)
            curs = ns
        return len(ans)


                    