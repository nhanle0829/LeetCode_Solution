class Solution:
    def encode(self, strs):
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        print(res)
        return res

    def decode(self, s):
        res = []
        index = 0
        while index < len(s):
            end = index
            while s[end] != '#':
                end += 1
            length = int(s[index: end])
            index = end + 1
            end = index + length
            res.append(s[index: end])
            index = end
        return res
