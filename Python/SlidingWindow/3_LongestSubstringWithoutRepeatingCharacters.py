class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited_char = set()
        longest = 0
        left = 0
        for right, char in enumerate(s):
            while s[right] in visited_char:
                visited_char.remove(s[left])
                left += 1
            visited_char.add(s[right])
            longest = max(longest, right - left + 1)
        return longest
