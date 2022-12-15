from typing import List


def findMinDifference(timePoints: List[str]) -> int:
    def convert(time):
        return int(time[:2]) * 60 + int(time[3:])
    minutes = sorted(map(convert, timePoints))
    minutes.append(1440 + minutes[0])
    return min((y - x) for x, y in zip(minutes, minutes[1:]))

if __name__ == '__main__':
    print(findMinDifference(["23:59","00:00"]))
