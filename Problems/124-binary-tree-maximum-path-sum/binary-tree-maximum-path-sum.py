# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -10001
        def helper(node) ->int:
            nonlocal ans
            if not node:
                return 0
            l = helper(node.left)
            r = helper(node.right)
            if l<r:l,r=r,l
            ans = max(ans,l+r+node.val,l+node.val,node.val)
            return max(0,node.val+l)
        helper(root)
        return ans

        
