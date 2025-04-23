# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return [0,0]
            a,b = dfs(node.left)
            x,y = dfs(node.right)
            return [b+y+node.val,max(a,b)+max(x,y)]
        a,b = dfs(root)
        return max(a,b)
        