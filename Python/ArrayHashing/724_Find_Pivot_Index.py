class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0
        for pivot, val in enumerate(nums):
            right_sum = total - left_sum - val
            if right_sum == left_sum:
                return pivot
            left_sum += val
        return -1