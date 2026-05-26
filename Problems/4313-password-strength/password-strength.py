class Solution:
    def passwordStrength(self, password: str) -> int:
        ans = 0
        for ch in set(password):
            if 'a'<=ch<='z':ans+= 1
            elif 'A'<=ch<='Z':ans+=2
            elif '0'<=ch<='9':ans+=3
            else: ans+=5
        return ans
        