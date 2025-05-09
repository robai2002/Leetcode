class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit,prvpof = 0,0
        profit_with_buy = -2000
        buy = 2000
        for v in prices:
            x = prvpof
            prvpof,profit = max(profit,prvpof),max(profit,profit_with_buy+v)
            if profit_with_buy + v<x:
                profit_with_buy = x-v
                buy = v

            profit_with_buy += max(0,buy - v)
            buy = min(v,buy)
            print(v,profit,prvpof,profit_with_buy,buy)
        return profit



        


            

            
