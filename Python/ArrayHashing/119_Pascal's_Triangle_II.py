class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        curr_row = [1]
        for i in range(1, rowIndex + 1):
            new_row = [1]
            for j in range(1, i):
                new_row.append(curr_row[j] + curr_row[j - 1])
            new_row.append(1)
            curr_row = new_row
        return curr_row
