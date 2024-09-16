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
