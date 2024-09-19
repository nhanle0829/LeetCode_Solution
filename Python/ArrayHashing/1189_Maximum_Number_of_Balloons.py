class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        text_counter = Counter(text)
        balloon_counter = Counter("balloon")
        max_balloon = float("inf")
        for char in balloon_counter:
            max_balloon = min(max_balloon, text_counter[char] // balloon_counter[char])
        return max_balloon
