class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_map = [0] * 26
        for char in chars:
            char_map[ord(char) - ord('a')] += 1

        res = 0
        for word in words:
            temp = char_map[:]
            good = True
            for char in word:
                index = ord(char) - ord('a')
                temp[index] -= 1
                if temp[index] < 0:
                    good = False
                    break
            if good:
                res += len(word)
        return res
