class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def backtrack(rows, cols, index):
            if index == len(word):
                return True
            if (rows < 0 or rows >= ROWS or
                    cols < 0 or cols >= COLS or
                    word[index] != board[rows][cols] or
                    (rows, cols) in path):
                return False

            path.add((rows, cols))
            res = (backtrack(rows + 1, cols, index + 1) or
                   backtrack(rows - 1, cols, index + 1) or
                   backtrack(rows, cols + 1, index + 1) or
                   backtrack(rows, cols - 1, index + 1))
            path.remove((rows, cols))
            return res

        for i in range(ROWS):
            for j in range(COLS):
                if backtrack(i, j, 0):
                    return True
        return False
