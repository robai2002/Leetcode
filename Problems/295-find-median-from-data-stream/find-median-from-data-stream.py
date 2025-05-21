class MedianFinder:

    def __init__(self):
        self.firstHeap=[]
        self.secondHeap=[]

    def addNum(self, num: int) -> None:
        if not self.firstHeap or num<-(self.firstHeap[0]):
            heapq.heappush(self.firstHeap,-num)
        else:
            heapq.heappush(self.secondHeap,num)   

        if len(self.firstHeap)>len(self.secondHeap)+1:
            element=-heapq.heappop(self.firstHeap)
            heapq.heappush(self.secondHeap,element)
        elif len(self.secondHeap)>len(self.firstHeap):
            element=heapq.heappop(self.secondHeap)
            heapq.heappush(self.firstHeap,-element)

    def findMedian(self) -> float:
        if len(self.firstHeap)>len(self.secondHeap):
            return -self.firstHeap[0]
        else:
            return (-(self.firstHeap[0])+self.secondHeap[0])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()