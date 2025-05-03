from collections import defaultdict
from typing import List

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # Coordinate Compression
        times = sorted(set(startTime + endTime))
        mp = {v: i+1 for i, v in enumerate(times)}  # 1-based indexing
        
        n = len(times) + 2
        dp = [0] * n
        jobs = []

        for s, e, p in zip(startTime, endTime, profit):
            jobs.append([mp[e], mp[s], p])  # [compressed_end, compressed_start, profit]

        jobs.sort()  # sort by end time ascending

        idx = 0
        for i in range(1, n):
            # carry forward the best profit so far
            dp[i] = dp[i - 1]
            # include all jobs ending at time i
            while idx < len(jobs) and jobs[idx][0] == i:
                end_idx, start_idx, p = jobs[idx]
                dp[i] = max(dp[i], dp[start_idx] + p)
                idx += 1

        return dp[n - 1]
