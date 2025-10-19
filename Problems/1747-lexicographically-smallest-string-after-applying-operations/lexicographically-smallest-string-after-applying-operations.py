from collections import deque

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        n = len(s)
        q = deque([s])
        seen = set()
        seen.add(s)
        res = s

        while q:
            curr = q.popleft()
            res = min(res, curr)

            op1 = list(curr)
            for i in range(1, n, 2):
                op1[i] = str((int(op1[i]) + a) % 10)
            op1 = "".join(op1)
            if op1 not in seen:
                seen.add(op1)
                q.append(op1)

            
            op2 = curr[-b:] + curr[:-b]
            if op2 not in seen:
                seen.add(op2)
                q.append(op2)

        return res