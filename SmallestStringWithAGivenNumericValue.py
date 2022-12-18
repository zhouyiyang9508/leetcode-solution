

def getSmallestString(n: int, k: int) -> str:
    res = ["a"] * n
    right = n - 1
    # already has n 'a'
    k -= n

    while right >= 0 and k > 0:
        # at most add 25 from to 'a' to 'z'
        to_add = min(k, 25)
        res[right] = chr(ord("a") + to_add)
        right -= 1
        k -= to_add

    return "".join(res)

if __name__ == '__main__':
    print(getSmallestString(3, 27))
    print(getSmallestString(5, 73))