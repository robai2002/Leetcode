class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        if (s1[0]!=s2[0] or s2[2]!=s1[2]) and (s1[0]!=s2[2] or s2[0]!=s1[2]):
            return False

        if (s1[1]!=s2[1] or s2[3]!=s1[3]) and (s1[1]!=s2[3] or s2[1]!=s1[3]):
            return False
        
        return True
