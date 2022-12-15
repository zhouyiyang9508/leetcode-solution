from typing import List
from collections import Counter

def numOfPairs(nums: List[str], target: str) -> int:
    counter = Counter(nums)
    ans = 0
    for key, freq in counter.items():
        if target.startswith(key):
            rest = target[len(key):]
            ans += counter[rest] * freq
            if key == rest:
                ans -= freq
    return ans


if __name__ == '__main__':
    print(numOfPairs(["123","4","12","34"], "1234") == 2)