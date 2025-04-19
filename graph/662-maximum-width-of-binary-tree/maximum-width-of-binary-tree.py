# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return False
        
        queue = deque([[root, 1]])
        res = 0

        while queue:
            level_len = len(queue)
            res = max(res, queue[-1][1] - queue[0][1] + 1)
            for _ in range(level_len):
                cur, val = queue.popleft()
                if cur.left:
                    queue.append([cur.left, val * 2])
                if cur.right:
                    queue.append([cur.right, val * 2 + 1])
        
        return res