class Solution:
    def isPathCrossing(self, path: str) -> bool:
        compass = {"N": (0, 1), "S": (0, -1), "E": (1, 0), "W": (-1, 0)}
        visited = {(0, 0)}
        curr = [0, 0]
        for direction in path:
            x, y = compass[direction]
            curr[0] += x;
            curr[1] += y
            if (curr[0], curr[1]) in visited:
                return True
            visited.add((curr[0], curr[1]))
        return False
