# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = 0
        
        def helper(node):
            if not node:
                return [10**6,-1]
            nonlocal ans
            x,y = helper(node.left)
            a,b = helper(node.right)
            x = min(a,x);y = max(y,b)
            ans = max(ans,node.val-x,y-node.val)
            return [min(x,node.val),max(y,node.val)]
        helper(root)
        return ans