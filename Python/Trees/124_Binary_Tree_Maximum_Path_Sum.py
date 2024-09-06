class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        def dfs(root):
            if root is None:
                return 0

            nonlocal res

            left_max = dfs(root.left)
            right_max = dfs(root.right)
            left_max = max(left_max, 0)
            right_max = max(right_max, 0)

            res = max(res, root.val + left_max + right_max)
            return root.val + max(left_max, right_max)

        dfs(root)
        return res