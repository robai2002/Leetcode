class Solution:
    def closestTarget(self, words: List[str], target: str, start: int) -> int:
        ans = len(words)
        n = len(words)
        for ind,word in enumerate(words):
            if word == target:
                ans = min(ans,(ind-start+n)%n ,(start-ind+n)%n)
        return ans if ans<n else -1