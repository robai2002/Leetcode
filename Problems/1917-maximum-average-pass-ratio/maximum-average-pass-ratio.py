class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:

        pq = []

        def get_new(x: int,y: int) ->float:
            return (x/y)-(x+1)/(y+1)
        

        for ind,(x,y) in enumerate(classes):
            heappush(pq,(get_new(x,y),ind))
        for e in range(extraStudents):
            gain,i = heapq.heappop(pq)
            classes[i][0] += 1
            classes[i][1] += 1
            heappush(pq,(get_new(classes[i][0],classes[i][1]),i)) 
        
        ans = sum (p/t for p,t in classes)
        return ans/len(classes)
        