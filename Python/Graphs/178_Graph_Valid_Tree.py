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
