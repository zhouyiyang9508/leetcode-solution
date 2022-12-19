from collections import Counter
from typing import List


def findAnagrams(s: str, p: str) -> List[int]:
    p_count = Counter(p)
    s_count = Counter()


    res = []
    for i in range(len(s)):
        s_count[s[i]] += 1
        # window size too large
        if i - len(p) >= 0:
            if s_count[s[i - len(p)]] == 1:
                del s_count[s[i - len(p)]]
            else:
                s_count[s[i - len(p)]] -= 1
        if s_count == p_count:
            res.append(i - len(p) + 1)

    return res

if __name__ == '__main__':
    print(findAnagrams("cbaebabacd", "abc"))
