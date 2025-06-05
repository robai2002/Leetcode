class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        hp = []
        for i,v in enumerate(heights[1:]):
            if v>heights[i]:
                heappush(hp,v-heights[i])
                if len(hp)>ladders:
                    bricks -= heappop(hp) 
                if bricks<0:
                    return i
        
        return len(heights)-1