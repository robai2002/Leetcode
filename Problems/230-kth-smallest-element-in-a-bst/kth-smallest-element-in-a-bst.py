# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.val = -1 
        self.ind = 0
        
        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            self.ind += 1
            if self.ind == k:
                self.val = node.val
                return 
            dfs(node.right)

        dfs(root)
        return self.val