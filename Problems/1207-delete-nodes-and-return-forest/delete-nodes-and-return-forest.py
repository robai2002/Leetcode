# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans = []
        def dfs(node,flg):
            if not node:
                return None
            if node.val in to_delete:
                dfs(node.left,True)
                dfs(node.right,True)
                return None
            elif flg:
                ans.append(node)
            node.left = dfs(node.left,False)
            node.right = dfs(node.right,False)
            return node
        dfs(root,True)
        return ans


        dfs(root,True)
        return ans 