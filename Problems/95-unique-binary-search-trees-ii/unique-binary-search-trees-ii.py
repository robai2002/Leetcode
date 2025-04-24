class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        memo = {}
        def sub_tree(left: int, right: int):
            if left > right:
                return [None]
            if (left, right) in memo:
                return memo[(left, right)]
            result = []
            for i in range(left, right + 1):
                left_sub = sub_tree(left, i - 1)
                right_sub = sub_tree(i + 1, right)
                for l in left_sub:
                    for r in right_sub:
                        node = TreeNode(i)
                        node.left = l
                        node.right = r
                        result.append(node)
            memo[(left, right)] = result
            return result
        return sub_tree(1, n)
