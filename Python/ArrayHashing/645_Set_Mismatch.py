class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        res = [0, 0]  # duplicate, missing
        hash_set = [0] * len(nums)
        for num in nums:
            if hash_set[num - 1] == 1:
                res[0] = num
            hash_set[num - 1] += 1
        for i in range(len(nums)):
            if hash_set[i] == 0:
                res[1] = i + 1
        return res
