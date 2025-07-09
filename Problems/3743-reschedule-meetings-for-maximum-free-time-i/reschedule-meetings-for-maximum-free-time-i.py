class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        duration = [0]
        for x,y in zip(startTime,endTime):
            duration.append(y-x)
            duration[-1] += duration[-2]
        startTime.append(eventTime)
        endTime = [0] + endTime
        ans = 0
        print(duration)
        for i in range(n+1):
            x = min(n,i+k)
            ans = max(ans,startTime[x]-duration[x]+duration[i] - endTime[i])
            #print(i,x,ans)
        return ans
