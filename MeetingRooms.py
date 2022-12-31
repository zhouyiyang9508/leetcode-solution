from typing import List


def canAttendMeetings(intervals: List[List[int]]) -> bool:
    # sort the intervals in non-descending order with the first element
    intervals.sort(key=lambda x:x[0])

    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False
    return True

if __name__ == '__main__':
    print(canAttendMeetings([[0,30],[5,10],[15,20]]))