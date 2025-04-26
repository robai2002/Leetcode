# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], Sum: int) -> int:
        s = defaultdict(int)
        s[0] = 1
        def tree(node,d):
            if not node:
                return 0
            d+=node.val
            print(node.val,d,d-Sum,s[d-Sum])
            c = s[d-Sum]
            s[d] += 1
            c +=tree(node.left,d)+tree(node.right,d)
            s[d] -=1
            return c
        
        return tree(root,0)