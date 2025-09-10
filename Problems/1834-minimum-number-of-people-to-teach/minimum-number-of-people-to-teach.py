from typing import List
from collections import defaultdict

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        langs = [set(l) for l in languages]
        
        candidates = set()
        for u, v in friendships:
            if langs[u-1].intersection(langs[v-1]):
                continue 
            candidates.add(u-1)
            candidates.add(v-1)
        
        if not candidates:  
            return 0
        
      
        ans = float("inf")
        for lang in range(1, n+1):
            teach_count = 0
            for user in candidates:
                if lang not in langs[user]:
                    teach_count += 1
            ans = min(ans, teach_count)
        
        return ans
