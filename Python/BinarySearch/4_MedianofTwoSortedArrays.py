class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A

        half = (len(A) + len(B)) // 2
        left_A, right_A = 0, len(A) - 1
        while True:
            mid_A = left_A + (right_A - left_A) // 2
            mid_B = half - mid_A - 2

            A_right = A[mid_A + 1] if mid_A + 1 < len(A) else float("inf")
            A_left = A[mid_A] if mid_A >= 0 else float("-inf")
            B_right = B[mid_B + 1] if mid_B + 1 < len(B) else float("inf")
            B_left = B[mid_B] if mid_B >= 0 else float("-inf")
            if A_left <= B_right and B_left <= A_right:
                if (len(A) + len(B)) % 2 == 0:
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2
                return min(A_right, B_right)
            if A_left > B_right:
                right_A = mid_A - 1
            else:
                left_A = mid_A + 1
