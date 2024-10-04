class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res = []
        seen = set(nums1)
        for num in nums2:
            if num in seen:
                res.append(num)
                seen.remove(num)
        return res
