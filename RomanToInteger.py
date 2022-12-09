values = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


def romanToInt(s: str) -> int:
    ans = values[s[-1]]
    # reverse from last second char
    for i in reversed(range(len(s) - 1)):
        if values[s[i]] < values[s[i + 1]]:
            ans -= values[s[i]]
        else:
            ans += values[s[i]]
    return ans

if __name__ == '__main__':
    print(romanToInt("III") == 3)
    print(romanToInt("MCMXCIV") == 1994)
    print(romanToInt("LVIII") == 58)


