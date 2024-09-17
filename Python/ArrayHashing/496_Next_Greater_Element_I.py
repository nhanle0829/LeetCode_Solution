class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash_map = {}
        for i, n in enumerate(nums1):
            hash_map[n] = i

        ans = [-1] * len(nums1)
        stack = []
        for num in nums2:
            while stack and num > stack[-1]:
                val = stack.pop()
                ans[hash_map[val]] = num
            if num in hash_map:
                stack.append(num)
        return ans