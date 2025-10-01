class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = 0
        while numBottles>=numExchange:
            ans += numBottles - numBottles%numExchange
            numBottles -= (numBottles//numExchange)*(numExchange-1) 
        return numBottles + ans