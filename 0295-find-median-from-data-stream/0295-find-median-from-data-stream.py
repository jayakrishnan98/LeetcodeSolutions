import heapq
class MedianFinder:
    def __init__(self):
        self.small, self.large  = [], []   # max heap
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)

        if len(self.large) and self.large[0] < -self.small[0]:
            small_pop = -heapq.heappop(self.small)
            large_pop = heapq.heappop(self.large)

            heapq.heappush(self.small, -large_pop)
            heapq.heappush(self.large, small_pop)
        
        if len(self.small) > len(self.large) + 1:
            num = -heapq.heappop(self.small)
            heapq.heappush(self.large, num)

        elif len(self.large) > len(self.small):
            num = heapq.heappop(self.large)
            heapq.heappush(self.small, -num)


    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        else:
            return (-self.small[0] + self.large[0]) / 2
