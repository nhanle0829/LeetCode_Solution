class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        res = [""] * numRows
        down = False
        curr_row = 0
        for c in s:
            res[curr_row] += c
            if curr_row == 0 or curr_row == numRows - 1:
                down = not down
            curr_row += 1 if down else -1
        return ''.join(res)
