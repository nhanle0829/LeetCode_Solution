class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = [[] for crs in range(numCourses)]
        in_degree = [0] * numCourses
        for crs, pre in prerequisites:
            adj_list[pre].append(crs)
            in_degree[crs] += 1

        res = []
        queue = collections.deque(i for i in range(numCourses) if in_degree[i] == 0)
        count = 0
        while queue:
            current = queue.popleft()
            res.append(current)
            count += 1
            for nei in adj_list[current]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    queue.append(nei)
        return res if count == numCourses else []


class Solution2:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_map = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)

        output = []
        visited, cycle = set(), set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True

            visited.add(crs)
            cycle.add(crs)
            for pre in pre_map[crs]:
                if not dfs(pre):
                    return False

            output.append(crs)
            cycle.remove(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return output
