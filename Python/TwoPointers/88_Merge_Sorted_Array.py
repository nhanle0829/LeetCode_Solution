class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        n1, n2 = m - 1, n - 1
        n1_end = m + n - 1
        while n1 >= 0 and n2 >= 0:
            if nums1[n1] > nums2[n2]:
                nums1[n1_end] = nums1[n1]
                n1 -= 1
            else:
                nums1[n1_end] = nums2[n2]
                n2 -= 1
            n1_end -= 1

        while n2 >= 0:
            nums1[n1_end] = nums2[n2]
            n2 -= 1
            n1_end -= 1
