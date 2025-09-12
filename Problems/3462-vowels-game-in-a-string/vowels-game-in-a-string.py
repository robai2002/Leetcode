class Solution:
    def doesAliceWin(self, s: str) -> bool:
        x = sum([1 for c in s if c in "aeiou"])
        return x>0