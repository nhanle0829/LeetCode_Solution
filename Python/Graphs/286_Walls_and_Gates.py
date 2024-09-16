class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        queue = collections.deque()
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    visited.add((r, c))

        distance = 0
        while queue:
            for i in range(len(queue)):
                row, col = queue.popleft()
                grid[row][col] = distance
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r < 0 or r >= ROWS or
                            c < 0 or c >= COLS or
                            grid[r][c] == -1 or
                            (r, c) in visited):
                        continue
                    visited.add((r, c))
                    queue.append((r, c))
            distance += 1
