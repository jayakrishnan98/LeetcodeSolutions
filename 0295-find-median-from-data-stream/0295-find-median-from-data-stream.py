import heapq
class MedianFinder:
    def __init__(self):
        self.small = []   # max heap
        self.large = []   # min heap
    def addNum(self, num: int) -> None:
        # Step 1: Put num into the left/smaller half
        heapq.heappush(self.small, -num)
        # Step 2: Make sure every element in small <= every element in large
        if self.large and (-self.small[0] > self.large[0]):
            small_top = -heapq.heappop(self.small)
            large_top = heapq.heappop(self.large)

            heapq.heappush(self.small, -large_top)
            heapq.heappush(self.large, small_top)
        # Step 3: Balance the sizes
        if len(self.small) > len(self.large) + 1:
            num = -heapq.heappop(self.small)
            heapq.heappush(self.large, num)

        elif len(self.large) > len(self.small):
            num = heapq.heappop(self.large)
            heapq.heappush(self.small, -num)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2