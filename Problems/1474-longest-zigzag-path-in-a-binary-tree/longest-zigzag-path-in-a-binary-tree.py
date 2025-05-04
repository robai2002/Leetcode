class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        ans = 0
        def dfs(node,isleft):
            nonlocal ans
            if not node:
                return 0
            a = dfs(node.left,False)
            b = dfs(node.right,True)
            ans = max(a,b,ans)
            if isleft:
                return a+1
            return b+1
        

        return max( dfs(root.left,False),dfs(root.right,True),ans)