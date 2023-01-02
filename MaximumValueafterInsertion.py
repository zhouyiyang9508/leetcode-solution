

def maxValue(n: str, x: int) -> str:
    if n[0] == '-':
        index = 1
        while index < len(n) and int(n[index]) <= x:
            index += 1
    else:
        index = 0
        while index < len(n) and int(n[index]) >= x:
            index += 1
    ans = n[:index] + str(x) + n[index:]
    return ans


if __name__ == '__main__':
    print(maxValue('-13', 2))
    print(maxValue('99', 9))