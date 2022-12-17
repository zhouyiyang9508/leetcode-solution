

def myPow(x: float, n: int) -> float:
    if n < 0:
        n = -n
        x = 1 / x
    res = 1
    while n:
        # n is odd, times extra x
        if n % 2 != 0:
            res *= x
        x *= x
        n //= 2

    return res


if __name__ == '__main__':
    print(myPow(2.0, -2) == 0.25)