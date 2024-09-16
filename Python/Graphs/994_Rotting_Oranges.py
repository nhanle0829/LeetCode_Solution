class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = collections.deque()
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r, c))

        minute = 0
        while queue and fresh > 0:
            minute += 1
            for i in range(len(queue)):
                row, col = queue.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r < 0 or r >= ROWS or
                            c < 0 or c >= COLS or
                            grid[r][c] != 1):
                        continue
                    grid[r][c] = 2
                    fresh -= 1
                    queue.append((r, c))
        return minute if not fresh else -1
