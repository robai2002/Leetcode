# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node: Optional[TreeNode])->int:
            if not node:
                return 0
            return node.val + dfs(node.left) + dfs(node.right)

        def dfs1(node:Optional[TreeNode],s: int):
            if not node:
                return 0,0
            a,b = dfs1(node.left,s)
            x,y = dfs1(node.right,s)
            p = b+y+node.val
            
            if abs(s-2*p)<abs(s-2*x) and abs(s-2*p)<abs(s-2*a):
                # print(node.val,a,b,x,y,p,p)
                return p,p
            elif abs(s-2*a)<abs(s-2*x):
               # print(node.val,a,b,x,y,a,p,end = "a \n")
                return a,p
            else:
               # print(node.val,a,b,x,y,b,p,end = " b\n")
                return x,p

        s = dfs(root)
        #print(root.right.right)
        d1,d2 = dfs1(root,s)
        return d1*(s-d1)%(10**9+7)
        
        
        