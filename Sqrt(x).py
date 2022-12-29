

def mySqrt(x: int) -> int:
    if x <= 1:
        return x
    left, right = 0, x
    while left < right:
        mid = (right + left) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid
    return left - 1

if __name__ == '__main__':
    print(mySqrt(8))
    print(mySqrt(9))