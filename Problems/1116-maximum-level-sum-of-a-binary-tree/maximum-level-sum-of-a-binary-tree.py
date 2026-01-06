# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        m = root.val
        level = 1
        ans = 1
        while queue:
            l = len(queue)
            s = 0 
            next_level = []
            for i in range(l):
                temp = queue.pop()
                s += temp.val
                if temp.right:
                    next_level.append(temp.right)
                if temp.left: 
                    next_level.append(temp.left)
            
            if s>m:
                ans = level
                m = s
            level += 1
            queue = next_level
        return ans
            
