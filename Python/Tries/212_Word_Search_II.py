class TrieNode:
    def __init__(self):
        self.root = {}

    def add_word(self, word):
        curr = self.root
        for char in word:
            if char not in curr:
                curr[char] = {}
            curr = curr[char]
        curr["end"] = True

    def remove_word(self, word):

        def dfs(i, root):
            if i >= len(word):
                del root["end"]
                return
            dfs(i + 1, root[word[i]])
            if not root[word[i]]:
                del root[word[i]]

        dfs(0, self.root)

    def is_word(self, node):
        return "end" in node


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.add_word(word)

        ROWS, COLS = len(board), len(board[0])
        res = []
        path = set()

        def dfs(row, col, node, word):
            if (row < 0 or row >= ROWS or
                    col < 0 or col >= COLS or
                    (row, col) in path or
                    board[row][col] not in node):
                return

            path.add((row, col))
            word += board[row][col]
            node = node[board[row][col]]
            if root.is_word(node):
                res.append(word)
                root.remove_word(word)

            dfs(row + 1, col, node, word)
            dfs(row - 1, col, node, word)
            dfs(row, col + 1, node, word)
            dfs(row, col - 1, node, word)
            path.remove((row, col))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root.root, "")
        return res