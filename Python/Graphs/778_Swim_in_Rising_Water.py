class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        N = len(grid)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        visited = set()  # (i, j)
        visited.add((0, 0))
        min_heap = [(grid[0][0], 0, 0)]
        while min_heap:
            time, i, j = heapq.heappop(min_heap)
            if i == N - 1 and j == N - 1:
                return time

            for x, y in directions:
                r = i + x
                c = j + y
                if r < 0 or r >= N or c < 0 or c >= N or (r, c) in visited:
                    continue
                visited.add((r, c))
                heapq.heappush(min_heap, (max(grid[r][c], time), r, c))
