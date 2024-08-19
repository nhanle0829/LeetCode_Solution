class Solution:
    def productExceptSelf(self, nums):
        res = [1] * len(nums)
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                continue
            prefix[i] = prefix[i - 1] * nums[i - 1]

        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                continue
            postfix[i] = postfix[i + 1] * nums[i + 1]

        for i in range(len(nums)):
            res[i] = prefix[i] * postfix[i]
        return res
