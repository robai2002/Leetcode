class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        odd,even = sorted(s1[1::2]),sorted(s1[::2])
        odd1,even1 = sorted(s2[1::2]),sorted(s2[::2])
        
        return odd == odd1 and even == even1
        