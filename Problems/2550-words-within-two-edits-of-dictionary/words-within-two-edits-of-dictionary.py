class Solution:
      def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def matches(query, target):
            n = len(query)
            misses = 0
            for i in range(n):
                if query[i] == target[i]:
                    continue
                misses += 1
                if misses > 2:
                    return False
            return True

        res = []
        for query in queries:
            for word in dictionary:
                if matches(query, word):
                    res.append(query)
                    break
        return res