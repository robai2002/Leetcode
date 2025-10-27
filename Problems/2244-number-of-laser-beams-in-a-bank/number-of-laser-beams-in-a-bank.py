class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        counts = [s.count('1') for s in bank if s.count('1')>0]
        return sum(a * b for a, b in zip(counts, counts[1:]))
        