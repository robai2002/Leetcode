# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dp  = []
        ans = 0
        def dfs(root,width,val) -> None:
            if not root:return 
            nonlocal ans
            if len(dp) == width:
                dp.append(val)
            ans = max(val - dp[width]+1,ans)
            dfs(root.left,width+1,val*2)
            dfs(root.right,width+1,val*2 + 1)
            return 
        dfs(root,0,1)
        return ans