class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        combine_sum = []

        def backtrack(index, total):
            if total == target:
                res.append(combine_sum.copy())
                return
            if total > target or index >= len(candidates):
                return

            combine_sum.append(candidates[index])
            backtrack(index + 1, total + candidates[index])
            combine_sum.pop()

            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1
            backtrack(index + 1, total)

        backtrack(0, 0)
        return res
