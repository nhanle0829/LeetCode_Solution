class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        weighted_graph = {i: [] for i in range(N)}
        for i in range(N - 1):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                distance = abs(x1 - x2) + abs(y1 - y2)
                weighted_graph[i].append([distance, j])
                weighted_graph[j].append([distance, i])

        result = 0
        node = 0
        heap = [[0, 0]]
        visited = set()
        while node < N:
            distance, u = heapq.heappop(heap)
            if u in visited:
                continue
            visited.add(u)
            node += 1
            result += distance
            for distance, v in weighted_graph[u]:
                if v not in visited:
                    heapq.heappush(heap, [distance, v])
        return result
