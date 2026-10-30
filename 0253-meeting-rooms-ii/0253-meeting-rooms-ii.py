class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        if not intervals:
            return 0

        intervals.sort(key= lambda x: x[0])

        occupied_room_time = []
        
        heapq.heappush(occupied_room_time, intervals[0][1])

        for interval in intervals[1:]:
            if occupied_room_time[0] <= interval[0]:

                heapq.heappop(occupied_room_time)

            heapq.heappush(occupied_room_time, interval[1])
            print(occupied_room_time)

        return len(occupied_room_time)