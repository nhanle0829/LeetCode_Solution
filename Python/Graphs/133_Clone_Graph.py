from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new = {}

        def dfs(node):
            if node in old_to_new:
                return old_to_new[node]

            new_node = Node(node.val)
            old_to_new[node] = new_node

            new_node.neighbors = [dfs(nei) for nei in node.neighbors]
            return new_node

        return dfs(node) if node else None
