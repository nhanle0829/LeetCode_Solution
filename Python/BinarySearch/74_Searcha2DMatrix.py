class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left_row, right_row = 0, len(matrix) - 1
        mid_row = 0
        while left_row <= right_row:
            mid_row = left_row + (right_row - left_row) // 2
            if target < matrix[mid_row][0]:
                right_row = mid_row - 1
            elif target > matrix[mid_row][-1]:
                left_row = mid_row + 1
            else:
                break

        if right_row < left_row:
            return False

        left_index, right_index = 0, len(matrix[0]) - 1
        while left_index <= right_index:
            mid_index = left_index + (right_index - left_index) // 2
            if target < matrix[mid_row][mid_index]:
                right_index = mid_index - 1
            elif target > matrix[mid_row][mid_index]:
                left_index = mid_index + 1
            else:
                return True

        return False
