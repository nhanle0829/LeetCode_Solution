class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.end_of_word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            index = ord(char) - ord('a')
            if not curr.children[index]:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.end_of_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            index = ord(char) - ord('a')
            if not curr.children[index]:
                return False
            curr = curr.children[index]
        return curr.end_of_word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            index = ord(char) - ord('a')
            if not curr.children[index]:
                return False
            curr = curr.children[index]
        return True