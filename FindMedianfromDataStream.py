from heapq import heappop, heappush

class MedianFinder:

    def __init__(self):
        self.low = []
        self.high = []

    def addNum(self, num: int) -> None:
        # push negative value of num to make min_heap a max_heap
        heappush(self.low, -num)
        heappush(self.high, -heappop(self.low))
        if len(self.low) < len(self.high):
            heappush(self.low, -heappop(self.high))

    def findMedian(self) -> float:
        if len(self.low) > len(self.high):
            return -self.low[0]
        else:
            return (-self.low[0] + self.high[0]) / 2.0

if __name__ == '__main__':
    median = MedianFinder()
    median.addNum(1)
    median.addNum(2)
    print(median.findMedian())
    median.addNum(3)
    print(median.findMedian())
