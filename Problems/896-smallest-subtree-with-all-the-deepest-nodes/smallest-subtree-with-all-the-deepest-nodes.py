# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        

        def dfs(node: Optional[TreeNode],val: int):
            if not node:
                return (None,val)
            
            a,x = dfs(node.left,val+1)
            b,y = dfs(node.right,val+1)
           # print(node.val,x,y,end = "  :: ")
            if x>y:
               # print(a,x)
                return (a,x)
            elif y>x:
               # print(b,y)
                return (b,y)
            else:
               # print(node.val,x)
                return (node,x)
        return dfs(root,0)[0]