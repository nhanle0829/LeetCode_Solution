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
            length = ''
            while s[index] != '#':
                length += s[index]
                index += 1
            length = int(length)
            res.append(s[index + 1: index + 1 + length])
            index += length + 1
        return res
