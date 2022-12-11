from collections import Counter


def lengthOfLongestSubstring(s: str) -> int:
    count = Counter()
    res = 0

    left = right = 0
    while right < len(s):
        r = s[right]
        count[r] += 1
        while count[r] > 1:
            l = s[left]
            count[l] -= 1
            left += 1
        res = max(res, right - left + 1)
        right += 1

    return res

if __name__ == '__main__':
    print(lengthOfLongestSubstring("pwwkew"))
