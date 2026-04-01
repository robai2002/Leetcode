class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        indices = list(range(n))
        indices.sort(key=lambda x: positions[x])
        stack = []
        for idx in indices:
            if directions[idx] == 'R':
                stack.append(idx)
            else:
                while stack and healths[idx] > 0:
                    if healths[idx] > healths[stack[-1]]:
                        healths[idx] -= 1
                        healths[stack.pop()] = 0
                    elif healths[stack[-1]] > healths[idx]:
                        healths[idx] = 0
                        healths[stack[-1]] -= 1
                    else:
                        healths[stack.pop()] = 0
                        healths[idx] = 0
        res = []
        for i in range(n):
            if healths[i] > 0:
                res.append(healths[i])
        return res


