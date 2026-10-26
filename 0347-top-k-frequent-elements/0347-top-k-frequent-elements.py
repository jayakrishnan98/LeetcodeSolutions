class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts = Counter(nums)
        min_heap = []

        for item, count in counts.items():
            heapq.heappush(min_heap, (count, item))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return [count for item, count in min_heap]

        
            