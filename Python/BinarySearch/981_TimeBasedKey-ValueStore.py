class TimeMap:

    def __init__(self):
        self.map = collections.defaultdict(list) #{"key": [("value", timestampt)]}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.map[key]
        left, right = 0, len(values) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return res