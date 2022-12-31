from typing import List


def intervalIntersection(firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
    l1, l2 = 0, 0
    result = []
    while l1 < len(firstList) and l2 < len(secondList):
        low = max(firstList[l1][0], secondList[l2][0])
        high = min(firstList[l1][1], secondList[l2][1])

        if high >= low:
            result.append([low, high])

        if firstList[l1][1] > secondList[l2][1]:
            l2 += 1
        else:
            l1 += 1
    return result


if __name__ == '__main__':
    print(intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]))