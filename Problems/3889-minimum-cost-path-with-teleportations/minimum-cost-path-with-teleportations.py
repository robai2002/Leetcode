class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        INF = 10**30
        cells = []
        for i in range(m):
            for j in range(n):
                idx = i * n + j
                cells.append((grid[i][j], idx))
        cells.sort(reverse=True)
        dist = [INF] * (m * n)
        dist[0] = 0
        best = INF
        for t in range(k + 1):
            for i in range(m):
                for j in range(n):
                    idx = i * n + j
                    cur = dist[idx]
                    if cur == INF:
                        continue
                    if j + 1 < n:
                        ni = idx + 1
                        cost = cur + grid[i][j + 1]
                        if cost < dist[ni]:
                            dist[ni] = cost
                    if i + 1 < m:
                        ni = idx + n
                        cost = cur + grid[i + 1][j]
                        if cost < dist[ni]:
                            dist[ni] = cost

            best = min(best, dist[m * n - 1])
            if t == k:
                break

            nextDist = [INF] * (m * n)
            move = INF

            p = 0
            while p < len(cells):
                val = cells[p][0]
                q = p

                group_min = INF
                while q < len(cells) and cells[q][0] == val:
                    group_min = min(group_min, dist[cells[q][1]])
                    q += 1

                move = min(move, group_min)

                for t2 in range(p, q):
                    idx = cells[t2][1]
                    nextDist[idx] = move

                p = q

            dist = nextDist

        return best if best < INF else -1