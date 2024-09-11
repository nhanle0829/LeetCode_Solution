class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for rowth in range(2, numRows + 1):
            new_row = [1]
            for i in range(rowth - 2):
                new_row.append(res[-1][i] + res[-1][i + 1])
            new_row.append(1)
            res.append(new_row)
        return res
