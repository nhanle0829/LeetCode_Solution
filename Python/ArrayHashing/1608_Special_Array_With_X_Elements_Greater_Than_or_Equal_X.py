class Solution:
    def specialArray(self, nums: List[int]) -> int:
        length = len(nums)
        count = [0] * (length + 1)
        for num in nums:
            index = min(length, num)
            count[index] += 1

        total_right = 0
        for i in range(length, 0, -1):
            total_right += count[i]
            if i == total_right:
                return i
        return -1
