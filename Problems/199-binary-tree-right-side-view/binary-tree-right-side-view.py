# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        def dfs(node,c,l):
            if not node:
                return l
            if len(l)==c:
                l.append(node.val)
            if node.right:
                 l = dfs(node.right,c+1,l)
            if node.left:
                l = dfs(node.left,c+1,l)
            return l




        return dfs(root,0,[])