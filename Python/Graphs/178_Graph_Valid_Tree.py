class Solution:
    def __find(self, vertex):
        root = self.subsets[vertex]
        while root != self.subsets[root]:
            root = self.subsets[root]
        while self.subsets[vertex] != root:
            nxt = self.subsets[vertex]
            self.subsets[vertex] = root
            vertex = nxt
        return root

    def __union(self, v1, v2):
        root1, root2 = self.__find(v1), self.__find(v2)
        if root1 != root2:
            self.subsets[root1] = root2
            self.component -= 1
            return True
        return False

    def validTree(self, n, edges):
        self.subsets = [i for i in range(n)]
        self.component = n

        for v1, v2 in edges:
            if not self.__union(v1, v2):
                return False
        return self.component == 1


class Solution2:
    def validTree(self, n, edges):
        adj_list = {i: [] for i in range(n)}
        for v1, v2 in edges:
            adj_list[v1].append(v2)
            adj_list[v2].append(v1)

        visited = set()

        def dfs(vertex, prev):
            if vertex in visited:
                return False

            visited.add(vertex)
            for nei in adj_list[vertex]:
                if nei == prev:
                    continue
                if not dfs(nei, vertex):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n
