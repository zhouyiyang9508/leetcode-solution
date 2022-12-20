import collections
from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    res = collections.defaultdict(list)

    for s in strs:
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord('a')] += 1
        res[tuple(count)].append(s)

    return res.values()

if __name__ == '__main__':
    print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))