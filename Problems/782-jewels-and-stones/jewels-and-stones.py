class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(1 for ch in stones if ch in jewels)