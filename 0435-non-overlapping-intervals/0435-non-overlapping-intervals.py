class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        
        intervals.sort(key = lambda x: x[1])

        ans = 0
        k = -inf

        for start, end in intervals:
            if start >= k:
                k = end
            else:
                ans += 1
        
        return ans