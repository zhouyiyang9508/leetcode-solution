def isOneEditDistance(s: str, t: str) -> bool:
    ls, lt = len(s), len(t)

    # make sure ls is larger than or equal to lt
    if lt > ls:
        isOneEditDistance(t, s)

    if ls - lt > 1:
        return False

    for i in range(lt):
        if s[i] != t[i]:
            # if the same length, can only replace
            if ls == lt:
                return s[i + 1:] == t[i + 1:]
            # if ls > lt, remove from ls
            else:
                return s[i + 1:] == t[i:]

    return lt + 1 == ls


if __name__ == '__main__':
    print(isOneEditDistance("abc", "ab"))
    print(isOneEditDistance("abcef", "ab"))
