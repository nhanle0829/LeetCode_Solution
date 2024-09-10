class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        permutation = []
        included = [False] * len(nums)

        def dfs(choices):
            if choices >= len(nums):
                res.append(permutation.copy())
                return

            for i in range(len(nums)):
                if not included[i]:
                    included[i] = True
                    permutation.append(nums[i])
                    dfs(choices + 1)

                    permutation.pop()
                    included[i] = False

        dfs(0)
        return res
