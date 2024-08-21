class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        left, right = 0, len(height) - 1
        while left < right:
            current_area = min(height[left], height[right]) * (right - left)
            area = max(area, current_area)
            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                left += 1
                right -= 1
        return area