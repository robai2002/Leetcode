class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        x = -k -1
        for ind,num in enumerate(nums):
            if num == 1:
                if x+k>=ind:
                    return False
                else: x = ind
        return True

        