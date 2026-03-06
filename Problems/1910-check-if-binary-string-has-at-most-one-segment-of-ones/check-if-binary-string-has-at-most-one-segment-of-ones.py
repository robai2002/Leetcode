class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        for ch,ch1 in pairwise(s):
            if ch =='0' and ch1 == '1':
                return False

        return True