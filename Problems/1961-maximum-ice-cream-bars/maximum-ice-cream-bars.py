class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        for ind,num in enumerate(costs):
            coins -= num
            if coins<0:return ind
        return len(costs)
        