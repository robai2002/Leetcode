# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:


        def ans(root:Optional[TreeNode]) ->List[int]:
            if not root:
                return [0,0]
            x,y = ans(root.left)
            a,b = ans(root.right)
            x+=a
            y+=b
            y = max(1,y*2)
            if root.val==1:
                x+= y
            return [x,y]

        return ans(root)[0]
        