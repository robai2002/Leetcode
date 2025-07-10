from sortedcontainers import SortedList
class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        ms = SortedList()
        n = len(startTime)

        endTime = [0] + endTime
        startTime.append(eventTime)

        for x,y in zip(startTime,endTime):
            ms.add(x-y)

        ans = 0

        for i in range(n):
            x = startTime[i] - endTime[i]
            y =  startTime[i+1]-endTime[i+1]
            z = endTime[i+1] - startTime[i]

            ms.remove(x)
            ms.remove(y)

            ind = bisect_left(ms,z)

            ans = max(startTime[i+1] - endTime[i] -z, ans)

            if ind < len(ms):
                ans = max(ans,startTime[i+1]- endTime[i], ans)
            
            ms.add(x)
            ms.add(y)
            
        return ans
