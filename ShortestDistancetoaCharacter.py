from typing import List


def shortestToChar(s: str, c: str) -> List[int]:
    prev = -float('inf')
    res = [float('inf')] * len(s)

    for i in range(len(s)):
        if s[i] == c:
            prev = i
        res[i] = i - prev

    prev = float('inf')
    for i in range(len(s) - 1, -1, -1):
        if s[i] == c:
            prev = i
        res[i] = min(res[i], prev - i)

    return res

if __name__ == '__main__':
    print(shortestToChar("loveleetcode", 'e'))
