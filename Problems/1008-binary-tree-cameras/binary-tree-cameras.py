# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        def get_ans(node):
            if not node:
                return [10**3,0,0]
            a = get_ans(node.left)
            b = get_ans(node.right)
            return [
                min(a)+min(b)+1,
            min(a[0]+min(b[:2]),b[0]+min(a[:2])),
            min(a[:2])+min(b[:2])
            ]
        return min(get_ans(root)[:2])