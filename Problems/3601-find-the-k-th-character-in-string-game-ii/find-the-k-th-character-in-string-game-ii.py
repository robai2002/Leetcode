class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        k -= 1
        c = 0
        n = k.bit_length()
        for i in reversed(range(n+1)):
            x = 1<<i
            if k&x:
                c += operations[i]
        
        c%=26
        return chr(ord('a')+c)