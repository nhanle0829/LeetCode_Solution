class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        hash_map = {}  # char: [start, end]
        for i, c in enumerate(s):
            if c not in hash_map:
                hash_map[c] = [i, i]
            else:
                hash_map[c][1] = i

        res = -1
        for start, end in hash_map.values():
            res = max(res, end - start - 1)
        return res
