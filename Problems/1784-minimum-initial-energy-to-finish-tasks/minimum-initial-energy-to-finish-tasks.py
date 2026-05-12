class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key = lambda x:(x[1]-x[0],x[1],x[0]))
        tasks[1:].sort(key = lambda x:(x[1],x[0]))
        
        ans = 0
        for x,y in tasks:
            ans = max(ans+x,y)
        return ans