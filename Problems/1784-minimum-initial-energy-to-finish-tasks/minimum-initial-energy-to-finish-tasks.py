class Solution:
    def minimumEffort(self, tasks):
        tasks.sort(key=lambda x: x[1] - x[0])
        need = 0
        for actual, minimum in tasks:
            need = max(minimum, need + actual)
        return need