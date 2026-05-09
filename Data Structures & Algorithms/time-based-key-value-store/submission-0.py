class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        store_value = (value, timestamp)

        if key in self.store:
            self.store[key].append(store_value)
        else:
            self.store[key] = [store_value]
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        left = 0
        right = len(self.store[key]) - 1

        while left <= right:
            mid = (left + right) // 2
            if self.store[key][mid][1] < timestamp:
                left = mid + 1
            elif self.store[key][mid][1] > timestamp:
                right = mid - 1
            else:
                return self.store[key][mid][0]

        if right < 0:
            return ""
        
        return self.store[key][right][0]
"""
alice: [(happy, 1), (sad, 3)]

1 3 5 8 10

while left <= right
    if mid == target
        return value associated with mid tuple

    if target <= mid
        right = mid - 1
    else
        left = mid + 1
"""