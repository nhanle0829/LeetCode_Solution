class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increased, decreased = True, True
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                increased = False
            if nums[i - 1] < nums[i]:
                decreased = False
        return increased or decreased
