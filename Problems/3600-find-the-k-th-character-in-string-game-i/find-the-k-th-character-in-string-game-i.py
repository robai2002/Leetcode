class Solution:
    def kthCharacter(self, k: int) -> str:
        k -= 1
        c = 0
        x = 1<<10
        while k:
            if k&x:
                c += 1
                k -= x
            x>>= 1
        c%=26
        return chr(ord('a')+c)