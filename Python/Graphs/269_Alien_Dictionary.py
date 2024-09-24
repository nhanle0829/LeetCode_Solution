class Solution:
    def alienOrder(self, words: list[str]) -> str:
        graph = {c: set() for word in words for c in word}

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            min_length = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_length] == w2[:min_length]:
                return ""
            for j in range(min_length):
                if w1[j] != w2[j]:
                    graph[w1[j]].add(w2[j])
                    break

        visited = {}  # True: in cycle, False: not in cycle
        res = []

        def dfs(u):
            if u in visited:
                return visited[u]

            visited[u] = True
            for v in graph[u]:
                if dfs(v):
                    return True
            res.append(u)
            visited[u] = False
            return False

        for c in graph:
            if dfs(c):
                return ""
        return "".join(res[::-1])
