class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack = []
        results = []
        for height in reversed(heights):
            items_popped = 0
            while stack and stack[-1] <= height:
                stack.pop()
                items_popped += 1
            results.append(items_popped + (1 if stack else 0))
            stack.append(height)

        return list(reversed(results))