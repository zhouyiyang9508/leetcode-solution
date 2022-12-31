from typing import List


def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    if not intervals:
        return [newInterval]
    i, n, start, end = 0, len(intervals), newInterval[0], newInterval[1]
    res = []
    while i < n and intervals[i][1] < start:
        res.append(intervals[i])
        i += 1

    while i < n and intervals[i][0] <= end:
        start = min(start, intervals[i][0])
        end = max(end, intervals[i][1])
        i += 1

    res.append([start, end])

    while i < n:
        res.append(intervals[i])
        i += 1

    return res

if __name__ == '__main__':
    print(insert([[1,3],[6,9]], [2,5]))
    print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))