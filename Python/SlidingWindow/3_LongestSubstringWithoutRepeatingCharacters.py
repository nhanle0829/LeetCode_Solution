class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited_char = set()
        longest = 0
        left = 0
        for right, char in enumerate(s):
            if char in visited_char:
                longest = max(longest, right - left)
                while s[left] != char:
                    visited_char.remove(s[left])
                    left += 1
                left += 1
            visited_char.add(char)
        return max(longest, len(s) - left)