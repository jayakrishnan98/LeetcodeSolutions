class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key= lambda x:x[0])
        min_heap = []

        heapq.heappush(min_heap, intervals[0][1])

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start >= min_heap[0]:
                heapq.heappop(min_heap)
            
            heapq.heappush(min_heap, end)
        
        return len(min_heap)
