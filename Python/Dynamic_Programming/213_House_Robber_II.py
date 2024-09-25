class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        rob1, rob2 = 0, 0
        for num in nums[1:]:
            rob2, rob1 = max(num + rob1, rob2), rob2
        attempt_1 = rob2

        rob1, rob2 = 0, 0
        for num in nums[:-1]:
            rob2, rob1 = max(num + rob1, rob2), rob2
        attempt_2 = rob2
        return max(attempt_1, attempt_2)
