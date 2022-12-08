import heapq


class Solution:
    def longestHappyString(self, a: int, b: int, c: int) -> str:
        heap = []
        for count, token in (-a, 'a'), (-b, 'b'), (-c, 'c'):
            if count:
                heapq.heappush(heap, (count, token))
        result = []
        while heap:
            count, token = heapq.heappop(heap)
            if len(result) > 1 and result[-2] == result[-1] == token:
                if not heap:
                    return ''.join(result)
                count, token = heapq.heapreplace(heap, (count, token))
            result.append(token)
            if count + 1:
                heapq.heappush(heap, (count + 1, token))

        return ''.join(result)



if __name__ == '__main__':
    print(Solution.longestHappyString(Solution, 3, 2, 1))
