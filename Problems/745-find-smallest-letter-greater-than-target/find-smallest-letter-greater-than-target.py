class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ch = bisect.bisect_right(letters,target)
        return letters[ch%(len(letters))]
        