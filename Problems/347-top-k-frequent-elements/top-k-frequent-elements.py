class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        l = [[y,x] for x,y in c.items()]
        l.sort(reverse = True)
        return [y for x,y in l[:k]]
