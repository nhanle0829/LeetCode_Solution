class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        left, right = 0, 1
        while right < len(nums):
            if nums[right] != nums[left]:
                nums[left + 1] = nums[right]
                left += 1
            right += 1
        return left + 1
