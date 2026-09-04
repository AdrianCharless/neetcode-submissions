class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.timeMap.get(key, []) == []:
            self.timeMap[key] = []
        self.timeMap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        values = self.timeMap.get(key, [])
        l = 0
        r = len(values) - 1
        res = ""
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                l = m + 1
                res = values[m][0]
            else:
                r = m - 1
        
        return res
