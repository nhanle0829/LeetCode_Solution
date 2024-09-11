class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_ST, map_TS = {}, {}
        for c1, c2 in zip(s, t):
            if (c1 in map_ST and map_ST[c1] != c2) or (c2 in map_TS and map_TS[c2] != c1):
                return False
            map_ST[c1] = c2
            map_TS[c2] = c1
        return True
