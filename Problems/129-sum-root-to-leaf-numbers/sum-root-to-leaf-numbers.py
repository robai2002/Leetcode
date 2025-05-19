# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        ans = 0
        def helper(node:Optional[TreeNode]) ->int:
            if not node:
                return 0
            nonlocal ans
            x = node.val
            y = helper(node.left) + helper(node.right)
     
            y = max(1,y*10)
            ans += x*y
            return y
        helper(root)
        return ans

