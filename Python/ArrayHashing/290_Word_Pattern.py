class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s):
            return False

        pattern_to_word, word_to_pattern = {}, {}
        for i in range(len(pattern)):
            if ((pattern[i] in pattern_to_word and pattern_to_word[pattern[i]] != s[i]) or
                    (s[i] in word_to_pattern and word_to_pattern[s[i]] != pattern[i])):
                return False
            pattern_to_word[pattern[i]] = s[i]
            word_to_pattern[s[i]] = pattern[i]
        return True
