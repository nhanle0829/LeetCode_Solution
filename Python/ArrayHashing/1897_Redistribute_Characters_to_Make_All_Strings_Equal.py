class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counter = {}
        for word in words:
            for char in word:
                counter[char] = counter.get(char, 0) + 1

        total = len(words)
        for char in counter:
            if counter[char] % total != 0:
                return False
        return True
