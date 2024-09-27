class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        res = set()
        for src, dst in paths:
            res.add(dst)
        for src, dst in paths:
            if src in res:
                res.remove(src)
        return list(res)[0]
