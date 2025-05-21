# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        
        def helper(node):
            if not node:
                return node 
            Left = helper(node.left)
            Right = helper(node.right)
            
            if Left:
                Left.right = node.right
                node.right = node.left
            node.left = None
            return Right if Right else Left if Left else node




        helper(root)


        

            