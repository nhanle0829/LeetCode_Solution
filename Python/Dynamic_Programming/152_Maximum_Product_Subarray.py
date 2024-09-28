class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res = nums[0]
        curr_min, curr_max = 1, 1
        for num in nums:
            temp = curr_max * num
            curr_max = max(temp, curr_min * num, num)
            curr_min = min(temp, curr_min * num, num)
            res = max(res, curr_max)
        return res
