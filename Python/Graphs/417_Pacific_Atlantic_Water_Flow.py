class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        ant, pac = set(), set()

        def bfs(r, c, visit, prev_height):
            if ((r, c) in visit or
                    r < 0 or r >= ROWS or
                    c < 0 or c >= COLS or
                    heights[r][c] < prev_height):
                return

            visit.add((r, c))
            bfs(r + 1, c, visit, heights[r][c])
            bfs(r - 1, c, visit, heights[r][c])
            bfs(r, c + 1, visit, heights[r][c])
            bfs(r, c - 1, visit, heights[r][c])

        for r in range(ROWS):
            bfs(r, 0, pac, 0)
            bfs(r, COLS - 1, ant, 0)

        for c in range(COLS):
            bfs(0, c, pac, 0)
            bfs(ROWS - 1, c, ant, 0)

        res = []
        for pair in pac:
            if pair in ant:
                res.append(list(pair))
        return res