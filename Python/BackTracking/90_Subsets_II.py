class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        subset = []

        def backtrack(index):
            if index >= len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[index])
            backtrack(index + 1)
            subset.pop()

            index += 1
            while index < len(nums) and nums[index] == nums[index - 1]:
                index += 1
            backtrack(index)

        backtrack(0)
        return res
