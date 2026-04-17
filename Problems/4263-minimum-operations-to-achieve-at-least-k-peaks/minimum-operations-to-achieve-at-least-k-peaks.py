class Solution:
    def minOperations(self, l: list[int], k: int) -> int:
        inf = 2 * 10**5
        n = len(l)
        if k * 2 > n: return -1
        l = [max(0, 1 - l[i] + max(l[i-1], l[i+1-n])) for i in range(n)]

        def f(l):
            l += [inf]
            ds = []
            stk = [inf]
            pp, p = inf + 1, inf + 2
            for v in l:
                while pp >= p <= v:
                    ds.append(p)
                    v += pp - p
                    p = stk.pop()
                    pp = stk.pop()
                stk.append(pp)
                pp, p = p, v
           
            ds.sort()
            return sum(ds[:k])

        return min(f(l[:-1]), f(l[1:]))