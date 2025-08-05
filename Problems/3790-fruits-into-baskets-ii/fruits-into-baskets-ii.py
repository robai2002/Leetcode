class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)
        dp = [True]*n
        ans = len(fruits)
        for fruit in fruits:
            for i,basket in enumerate(baskets):
                if dp[i] and fruit<=basket:
                    dp[i] = False
                    ans -= 1
                    break
        return ans
            