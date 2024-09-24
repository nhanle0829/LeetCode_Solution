class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list) # List[(weight, v)]
        for u, v, w in times:
            graph[u].append((w, v))

        time = 0
        min_heap = [(0, k)]
        visited = set()
        while min_heap:
            u_weight, u = heapq.heappop(min_heap)
            if u in visited:
                continue
            visited.add(u)
            time = max(u_weight, time)
            for v_weight, v in graph[u]:
                if v not in visited:
                    heapq.heappush(min_heap, (u_weight + v_weight, v))
        return time if len(visited) == n else -1
