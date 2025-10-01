class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        ans = 0
        while numBottles>=numExchange:
            numBottles -=(numExchange-1)
            ans += numExchange 
            numExchange += 1
        return numBottles + ans