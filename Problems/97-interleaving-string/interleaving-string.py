class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        @cache
        def ans(i: int, j: int, k: int, b: int) -> bool:
            if k == len(s3):
                return True
            if b:
                while k < len(s3) and j<len(s2) and s2[j] == s3[k]:
                    j += 1
                    k += 1
                    if ans(i, j, k, 1 - b):
                        return True
            else:
                while k<len(s3) and i<len(s1) and s1[i] == s3[k]:
                    i += 1
                    k += 1
                    if ans(i,j,k,1-b):
                        return True
            return False
            

        return ans(0, 0, 0, 0) | ans(0, 0, 0, 1)
