class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            if node is None:
                return 0
            res = 0
            if node.val >= max_val:
                res = 1
                max_val = node.val
            res += dfs(node.left, max_val)
            res += dfs(node.right, max_val)
            return res

        return dfs(root, root.val)
