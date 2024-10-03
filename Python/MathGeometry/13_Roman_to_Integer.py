class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        res = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
                res += roman_to_int[s[i + 1]] - roman_to_int[s[i]]
                i += 2
            else:
                res += roman_to_int[s[i]]
                i += 1
        return res
