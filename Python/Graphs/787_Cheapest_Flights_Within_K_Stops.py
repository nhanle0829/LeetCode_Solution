class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        queue = collections.deque([(src, 0)])
        prices[src] = 0
        k += 1
        while k > 0 and queue:
            for i in range(len(queue)):
                u, price_from_src = queue.popleft()
                for v, w in graph[u]:
                    new_price = price_from_src + w
                    if new_price < prices[v]:
                        prices[v] = new_price
                        queue.append((v, new_price))
            k -= 1
        return prices[dst] if prices[dst] != float("inf") else -1
