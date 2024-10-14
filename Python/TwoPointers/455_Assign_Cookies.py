class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        res = 0
        i, j = 0, 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                res += 1
                i += 1
            j += 1
        return res
