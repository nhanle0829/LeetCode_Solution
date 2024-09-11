class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        for char in s[::-1]:
            if char == ' ':
                if length >= 1:
                    return length
            else:
                length += 1
        return length
