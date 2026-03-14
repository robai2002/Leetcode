from collections import deque

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        if k > (3 << (n - 1)):
            return ""

        q = deque([""])

        while k:
            temp = q.popleft()

            for ch in ['a', 'b', 'c']:
                if not temp or temp[-1] != ch:
                    q.append(temp + ch)

                    if len(temp) + 1 == n:
                        k -= 1

                if k == 0:
                    break

        return q[-1]