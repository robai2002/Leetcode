class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ans = letters[0]
        for latter in letters:
            if target<latter:
                if ans<=target:
                    ans = latter
                elif ans>latter:
                    ans = latter
        return ans
        