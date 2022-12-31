import heapq
from typing import List


def minMeetingRooms(intervals: List[List[int]]) -> int:
    if not intervals:
        return 0

    intervals.sort(key=lambda x:x[0])
    rooms = []
    heapq.heappush(rooms, intervals[0][1])

    for i in intervals[1:]:
        if i[0] >= rooms[0]:
            heapq.heappop(rooms)
        heapq.heappush(rooms, i[1])

    return len(rooms)

if __name__ == '__main__':
    print(minMeetingRooms([[0,30],[5,10],[15,20]]))
