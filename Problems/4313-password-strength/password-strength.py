class Solution:
    def passwordStrength(self, password: str) -> int:
        ans = 0
        for ch in set(password):
            if ch.islower():ans+= 1
            elif ch.isupper():ans+=2
            elif ch.isdigit():ans+=3
            else: ans+=5
        return ans
        