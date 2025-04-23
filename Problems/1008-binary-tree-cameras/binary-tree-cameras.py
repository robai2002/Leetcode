# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node):
            nonlocal ans
            if not node:
                return 1
            l = dfs(node.left)
            r = dfs(node.right)
            if l ==2 or r==2 :
                ans += 1
                return 0
            else:
                return min(l,r)+1
        if dfs(root) == 2:
            ans += 1
        return ans
            