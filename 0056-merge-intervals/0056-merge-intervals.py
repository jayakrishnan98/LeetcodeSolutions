class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key = lambda x:x[0])
        result = []

        for interval in intervals:
            start, end = interval
            if not result or result[-1][1] < start:
                result.append(interval)
            else:
                result[-1][1] = end
            
        return result