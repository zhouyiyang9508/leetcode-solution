

def isLongPressedName(name: str, typed: str) -> bool:
    l1, l2 = 0, 0
    m, n = len(name), len(typed)
    while l1 < m and l2 < n:
        if name[l1] != typed[l2]:
            return False
        l1 += 1
        l2 += 1
        c1 = 0
        while l1 < m and name[l1] == name[l1 - 1]:
            c1 += 1
            l1 += 1
        c2 = 0
        while l2 < n and name[l2] == name[l2 - 1]:
            c2 += 1
            l2 += 1
        if c1 > c2:
            return False
    return l1 == m and l2 == n

if __name__ == '__main__':
    print(isLongPressedName("saeed", "ssaaedd"))