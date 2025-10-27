class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        l = [s.count('1') for s in bank if s.count('1')>0]
        return sum(l[i]*l[i+1] for i in range(len(l)-1))
        