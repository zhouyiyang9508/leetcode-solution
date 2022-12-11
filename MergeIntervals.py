from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:

    intervals.sort(key=lambda x:x[0])
    merged = []

    for interval in intervals:
        # first interval or has no overlapping with previous interval at all
        if not merged or interval[0] > merged[-1][1]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged


if __name__ == '__main__':
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print(merge(intervals))