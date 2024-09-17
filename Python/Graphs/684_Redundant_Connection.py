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
            self.subsets[root1] = self.subsets[root2]
            return True
        return False

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.subsets = [i for i in range(len(edges) + 1)]

        for v1, v2 in edges:
            if not self.__union(v1, v2):
                return [v1, v2]
