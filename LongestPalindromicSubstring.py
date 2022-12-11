
def longestPalindrome(s: str) -> str:
    # record max length and start index
    maximum = 0
    start = 0

    def expand(s, l, r):
        nonlocal maximum, start
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1

        if r - l - 1 > maximum:
            start = l + 1
            maximum = r - l - 1

    for i in range(len(s)):
        expand(s, i, i)
        expand(s, i, i + 1)

    return s[start:start+maximum]


if __name__ == '__main__':
    print(longestPalindrome("babad"))

