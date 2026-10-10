class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.arr.sort()

    def findMedian(self) -> float:
        if len(self.arr) % 2 == 0:
            i = (len(self.arr) - 1) // 2
            j = i + 1
            return (self.arr[i] + self.arr[j]) / 2 
        
        i = (len(self.arr) - 1) // 2
        return self.arr[i]

"""
[1 2 3 4]

3//2 = 1
"""
        
        