class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(index, total):
            if index >= len(candidates) or total > target:
                return

            if total == target:
                res.append(path[:])
                return

            path.append(candidates[index])
            dfs(index, total + candidates[index])

            path.pop()
            dfs(index + 1, total)

        dfs(0, 0)
        return res
