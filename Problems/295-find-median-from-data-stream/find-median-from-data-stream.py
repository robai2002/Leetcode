class MedianFinder:

    def __init__(self):
        self.mxhp = []
        self.mnhp = []
        self.length = 0

    def addNum(self, num: int) -> None:
        self.length += 1
        # print(self.mnhp,self.mxhp,end = " : ")
        if self.mnhp:
            mnmin = - heapq.heappop(self.mnhp)
            if num<mnmin:
                mnmin,num=num,mnmin
            heapq.heappush(self.mnhp,-mnmin)
        # print(self.mnhp,self.mxhp,end = " : ")
        heapq.heappush(self.mxhp,num)
        if len(self.mxhp) - len(self.mnhp)>1:
            x = heapq.heappop(self.mxhp)
            heapq.heappush(self.mnhp,-x)
        # print(self.mnhp,self.mxhp)


    def findMedian(self) -> float:
        # print(self.mnhp,self.mxhp)
        if not self.mxhp:
            return 0.0
        y = heapq.heappop(self.mxhp)
        heapq.heappush(self.mxhp,y)
        if self.length%2 ==0:
            x = heapq.heappop(self.mnhp)
            heapq.heappush(self.mnhp,x)
            y = (y-x)/2
        return y
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()