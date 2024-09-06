class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # return sorted(points, key=lambda x: x[0] ** 2 + x[1] ** 2)[:k]
        distances = [(point[0] ** 2 + point[1] ** 2, point[0], point[1]) for point in points]
        heapq.heapify(distances)
        res = []
        for i in range(k):
            distance, point1, point2 = heapq.heappop(distances)
            res.append([point1, point2])
        return res
