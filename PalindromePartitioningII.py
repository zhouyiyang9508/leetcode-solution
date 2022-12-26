def minCut(s: str) -> int:
    # dp[i] means minCut till index i
    dp = [0] * len(s)
    # the maximum cut in theory
    for i in range(1, len(s)):
        dp[i] = i

    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            newCut = 0 if left == 0 else dp[left - 1] + 1
            dp[right] = min(dp[right], newCut)
            left -= 1
            right += 1

    for i in range(len(s)):
        # expand from centers
        expand(i, i)
        expand(i - 1, i)

    return dp[len(s) - 1]


if __name__ == '__main__':
    print(minCut("aab"))
    print(minCut("a"))
    print(minCut("ab"))
