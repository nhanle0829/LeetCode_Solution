class Solution:
    def leastBricks(self, wall: list[list[int]]) -> int:
        gap = {0: 0}
        for row in wall:
            position = 0
            for brick in row[:-1]:
                position += brick
                gap[position] = gap.get(position, 0) + 1
        return len(wall) - max(gap.values())
