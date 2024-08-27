class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        min_value = nums[0]
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= nums[left]:
                min_value = min(min_value, nums[left])
                left = mid + 1
            else:
                right = mid - 1
                min_value = min(min_value, nums[mid])

        return min_value
