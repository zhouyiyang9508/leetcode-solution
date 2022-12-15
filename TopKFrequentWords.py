from typing import List
from heapq import heappop, heappush
from collections import Counter

class Pair:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    def __lt__(self, other):
        return self.freq < other.freq or (self.freq == other.freq and self.word > other.word)


def topKFrequent(words: List[str], k: int) -> List[str]:
    min_heap = []
    counter = Counter(words)

    for word, freq in counter.items():
        heappush(min_heap, Pair(word, freq))
        if len(min_heap) > k:
            heappop(min_heap)

    return [p.word for p in sorted(min_heap, reverse=True)]


if __name__ == '__main__':
    print(topKFrequent(['i', 'i', 'love', 'love', 'apple', 'from', 'amazon', 'fresh'], 2))


