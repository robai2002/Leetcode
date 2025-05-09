class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = [[-y,x] for x,y in collections.Counter(words).items()]
        c.sort()
        return [y for x,y in c[:k]]