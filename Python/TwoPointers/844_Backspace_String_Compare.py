class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def convert(s):
            res = []
            for char in s:
                if char == '#':
                    if res:
                        res.pop()
                else:
                    res.append(char)
            return res

        return convert(s) == convert(t)
