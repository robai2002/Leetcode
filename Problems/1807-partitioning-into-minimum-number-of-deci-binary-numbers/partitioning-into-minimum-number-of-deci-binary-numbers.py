class Solution:
    def minPartitions(self, n: str) -> int:
        mx = '0'
        for ch in n:
            mx = max(mx,ch)
        return ord(mx)-48

        