from typing import List

class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        
        def dfs(n: int, p1: int, p2: int):
            if p1 + p2 == n + 1:
                return (1, 1)
            
            if p1 > p2:
                p1, p2 = p2, p1
            
            if n <= 4:
                return (2, 2)

            # Next level length
            m = (n + 1) // 2

            minR, maxR = n, -n

            if p1 - 1 > n - p2:
                p1, p2 = n + 1 - p2, n + 1 - p1

            # Both in first half
            if p2 * 2 <= n + 1:
                a = p1 - 1
                b = p2 - p1 - 1
                
                for i in range(a + 1):
                    for j in range(b + 1):
                        x, y = dfs(m, i + 1, i + j + 2)
                        minR = min(minR, x + 1)
                        maxR = max(maxR, y + 1)
            
            # In different halves
            else:
                p4 = n + 1 - p2
                a = p1 - 1
                b = p4 - p1 - 1
                c = p2 - p4 - 1

                for i in range(a + 1):
                    for j in range(b + 1):
                        d = i + j + 1 + (c + 1) // 2 + 1
                        x, y = dfs(m, i + 1, d)
                        minR = min(minR, x + 1)
                        maxR = max(maxR, y + 1)

            return (minR, maxR)

        return list(dfs(n, firstPlayer, secondPlayer))
