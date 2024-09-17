class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = [[] for i in range(numCourses)]
        in_degree = [0] * numCourses

        for crs, pre in prerequisites:
            adj_list[pre].append(crs)
            in_degree[crs] += 1

        queue = collections.deque(i for i in range(numCourses) if in_degree[i] == 0)
        count = 0
        while queue:
            current = queue.popleft()
            count += 1
            for nei in adj_list[current]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    queue.append(nei)
        return count == numCourses


class Solution2:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)

        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            if not pre_map[crs]:
                return True

            visited.add(crs)
            for pre in pre_map[crs]:
                if not dfs(pre):
                    return False

            visited.remove(crs)
            pre_map[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True