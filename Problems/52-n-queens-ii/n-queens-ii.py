class Solution:
    def totalNQueens(self, n: int) -> int:
        col = list()
        pos = set()
        neg = set()
        m =  dict()
        l = []

        def helper(ind: int) -> int:
            if ind == n:
                return  1
            t = tuple(col)
            if t in m:
                return m[t]
            m[t] = 0
            for i in range(n):
                if i not in col:
                    if ind+i not in pos:
                        if ind -i not in neg:
                            pos.add(i+ind)
                            neg.add(ind-i)
                            col.append(i)
                            m[t] += helper(ind+1)
                            pos.remove(i+ind)
                            neg.remove(ind-i)
                            col.pop()
            return m[t]
        return helper(0)