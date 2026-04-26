class Solution:
    def countMonobit(self, n: int) -> int:
        n += 1
        ary = format(n, 'b')
        return len(ary)
        