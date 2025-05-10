import numpy as np
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2: return 0
        return int(np.max(np.diff(np.sort(nums))))