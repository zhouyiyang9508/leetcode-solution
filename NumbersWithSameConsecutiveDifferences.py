from typing import List


def numsSameConsecDiff(n: int, k: int) -> List[int]:
    queue = [x for x in range(1, 10)]

    # first digit is already defined, only need n - 1 times to get result
    for i in range(n - 1):
        next_queue = []
        for num in queue:
            tail_digit = num % 10
            next_digits = set([tail_digit + k, tail_digit - k])
            for next_digit in next_digits:
                if 0 <= next_digit < 10:
                    next_queue.append(num * 10 + next_digit)
        queue = next_queue

    return queue


if __name__ == '__main__':
    print(numsSameConsecDiff(3, 7))