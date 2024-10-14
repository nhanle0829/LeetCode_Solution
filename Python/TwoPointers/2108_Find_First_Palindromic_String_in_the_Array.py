class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        for word in words:
            if self.isPalidrome(word):
                return word
        return ""

    def isPalidrome(self, word):
        l, r = 0, len(word) - 1
        while l < r:
            if word[l] != word[r]:
                return False
            l += 1; r -= 1
        return True