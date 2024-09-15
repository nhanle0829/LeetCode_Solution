class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr:
                curr[char] = {}
            curr = curr[char]
        curr["end"] = True

    def search(self, word: str) -> bool:

        def dfs(index, root):
            curr = root
            for i in range(index, len(word)):
                if word[i] == '.':
                    for char in curr:
                        if char != "end" and dfs(i + 1, curr[char]):
                            return True
                    return False
                else:
                    if word[i] not in curr:
                        return False
                    curr = curr[word[i]]
            return "end" in curr

        return dfs(0, self.root)
