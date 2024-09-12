class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_to_char = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []

        def backtrack(i, curr_s):
            if len(curr_s) == len(digits):
                res.append(curr_s)
                return

            for char in num_to_char[digits[i]]:
                backtrack(i + 1, curr_s + char)

        if digits:
            backtrack(0, "")
        return res
